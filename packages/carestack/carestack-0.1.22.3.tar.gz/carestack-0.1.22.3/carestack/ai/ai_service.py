from datetime import datetime, timezone
import logging
from typing import Any, Dict, List, Type, TypeVar

from pydantic import BaseModel, ValidationError

from carestack.ai.ai_utils import AiUtilities
from carestack.base.base_service import BaseService
from carestack.base.base_types import ClientConfig
from carestack.base.errors import EhrApiError
from carestack.common.enums import AI_ENDPOINTS, HealthInformationTypes
from carestack.ai.ai_dto import (
    RadiologySummaryResponse,
    DischargeSummaryResponse,
    FhirBundleResponse,
    GenerateFhirBundleDto,
    ProcessDSDto,
)

_DTO_T = TypeVar("_DTO_T", bound=BaseModel)


class AiService(BaseService):
    """
    AiService provides a high-level interface for AI-powered healthcare document generation.

    ### This service enables SDK users to interact with CareStack AI endpoints for:
      - Generating discharge summaries (`generate_discharge_summary`)
      - Generating FHIR bundles (`generate_fhir_bundle`)

    !!! note "Key Features"
        - Validates input data using Pydantic models (`ProcessDSDto`, `GenerateFhirBundleDto`)
        - Handles encryption of sensitive data before transmission
        - Provides robust error handling and logging for all operations

    Methods:
        generate_discharge_summary(process_ds_data) : Generates a discharge summary from provided case data.
        generate_fhir_bundle(generate_fhir_bundle_data) : Generates a FHIR-compliant bundle from provided case data.

    Args:
        config (ClientConfig): API credentials and settings for service initialization.

    Raises:
        EhrApiError: For validation, API, or unexpected errors during operations.

    Example Usage:
        ```
        config = ClientConfig(
            api_key="your_api_key",
        )
        service = AiService(config)
        summary = await service.generate_discharge_summary({...})
        bundle = await service.generate_fhir_bundle({...})
        ```


    """

    def __init__(self, config: ClientConfig):
        super().__init__(config)
        self.logger = logging.getLogger(__name__)
        self.utilities = AiUtilities(config)

    async def _validate_data(
        self, dto_type: Type[_DTO_T], request_data: dict[str, Any]
    ) -> _DTO_T:
        """
        Validate dictionary data against a Pydantic model.

        This internal utility ensures that the provided dictionary matches the expected schema for the AI API.
        Raises an EhrApiError if validation fails.

        Args:
            dto_type (Type[_DTO_T]): The Pydantic model class to validate against.
            request_data (dict): The data to validate.

        Returns:
            _DTO_T: An instance of the validated Pydantic model.

        ### Raises:
            EhrApiError: If validation fails.
        """
        try:
            validated_instance: _DTO_T = dto_type(**request_data)
            return validated_instance
        except ValidationError as err:
            self.logger.error(
                f"Pydantic validation failed: {err.errors()}", exc_info=True
            )
            raise EhrApiError(f"Validation failed: {err.errors()}", 400) from err

    async def generate_case_summary(
        self, process_data: dict[str, Any], case_type: str
    ) -> DischargeSummaryResponse:
        """
        Generic case summary generator for all case types (DischargeSummary, OpConsultation, Radiology).
        """
        self.logger.info(f"Starting generation of {case_type} summary with data: {process_data}")

        try:
            process_dto: ProcessDSDto = await self._validate_data(ProcessDSDto, process_data)

            # Throw error if no encryptedData or files
            if not process_dto.encrypted_data and not process_dto.files:
                raise ValueError("No files or encrypted data provided.")

            # Use encryptedData if provided, else encrypt files
            if process_dto.encrypted_data:
                encrypted_data = process_dto.encrypted_data
            else:
                payload_to_encrypt = {"files": process_dto.files}
                encrypted_data = await self.utilities.encryption(payload=payload_to_encrypt)

            payload = {
                "caseType": case_type,
                "encryptedData": encrypted_data,
            }

            if process_dto.public_key:
                payload["publicKey"] = process_dto.public_key
            response: DischargeSummaryResponse = await self.post(
                AI_ENDPOINTS.GENERATE_DISCHARGE_SUMMARY,
                payload,
                response_model=DischargeSummaryResponse,
            )

            return response

        except EhrApiError as e:
            self.logger.error(f"EHR API Error during {case_type} summary generation: {e.message}", exc_info=True)
            raise
        except ValueError as e:
            self.logger.error(f"Validation error in {case_type} summary generation: {e}", exc_info=True)
            raise EhrApiError(str(e), 422) from e
        except Exception as error:
            error_message = str(error)
            self.logger.error(f"Unexpected error in {case_type} summary generation: {error_message}", exc_info=True)
            raise EhrApiError(
                f"An unexpected error occurred while generating {case_type} summary: {error_message}", 500
            ) from error


    async def generate_fhir_bundle(self, data: dict[str, Any]) -> dict[str, Any]:
        """
        Generates a FHIR bundle based on the provided data.

        This method validates and processes the input, encrypts extracted data if necessary, and sends it to the AI API
        to generate a FHIR-compliant bundle. Use this method to automate generation of interoperable FHIR bundles from structured clinical data.

        Attributes:
            generate_fhir_bundle_data (GenerateFhirBundleDto): GenerateFhirBundleDto containing required inputs for generating the bundle.

        ### Args:
            generate_fhir_bundle_data (dict): Dictionary containing:
                - caseType (str): Type of the case (`inpatient`, `outpatient`, etc.)
                - enableExtraction (bool): Flag to enable data extraction from provided documents.
                - documentReferences (list[str]): List of document references to include in the bundle.
                - recordId (Optional[str]): Unique identifier for the record.
                - extractedData (Optional[dict]): Structured clinical data to generate the bundle.
                - encryptedData (Optional[str]): If provided, skips encryption and uses this encrypted payload.
                - publicKey (Optional[str]): Required if using `extractedData` without pre-encryption.

        ### Returns:
            dict[str, Any]: The generated FHIR-compliant bundle.
                Example:
                {
                    "resourceType": "Bundle",
                    "type": "document",
                    "entry": [
                        {
                            "resource": {
                                "resourceType": "Patient",
                                "id": "123",
                                ...
                            }
                        },
                        ...
                    ]
                }

        Raises:
            ValidationError: If input fails Pydantic model validation.
            EhrApiError: Raised on API failure (status 400/422/500).
            ValueError: If both `extractedData` and `encryptedData` are missing.

        ### Example (Success):

            response = await service.generate_fhir_bundle({
                "caseType": "DischargeSummary",
                "enableExtraction": True,
                "documentReferences": ["doc123", "doc456"],
                "recordId": "rec-789",
                "extractedData": {
                    "patientName": "John Doe",
                    "diagnosis": "Hypertension",
                    "treatment": "Medication and lifestyle changes"
                },
                "publicKey": "-----BEGIN PUBLIC KEY-----...",
            })

            print(response)

            Output will look like:

            {
                "resourceType": "Bundle",
                "entry": [
                    {"resource": {"resourceType": "Patient", "id": "123", ...}},
                    ...
                ]
            }

        ### Example (Validation Failure):

            await service.generate_fhir_bundle({
                "caseType": "DischargeSummary"
            })
            # Raises EhrApiError: No extracted data or encrypted data provided (422)
        """
        self.logger.info(f"Starting generation of FHIR bundle with data: {data}")
        try:
            validated_data: GenerateFhirBundleDto = await self._validate_data(
                GenerateFhirBundleDto, data
            )
            encryption_payload: dict[str, Any] = {}
            if validated_data.enable_extraction:
                if not validated_data.extracted_data:
                    raise ValueError("No extracted data is provided.")
                else:
                    encryption_payload["extractedData"] = validated_data.extracted_data
            else:
                if validated_data.patient_details and validated_data.doctors_details:
                    encryption_payload["patientDetails"] = (
                        validated_data.patient_details.model_dump(by_alias=True)
                    )
                    encryption_payload["practitionersDetails"] = [
                        doc.model_dump(by_alias=True)
                        for doc in validated_data.doctors_details
                    ]
                else:
                    raise ValueError("patient and practitioner details are required.")

            encryption_payload["documentReferences"] = (
                validated_data.document_references
            )
            encryptedData = await self.utilities.encryption(payload=encryption_payload)

            payload = {
                "caseType": validated_data.case_type,
                "enableExtraction": validated_data.enable_extraction,
                "encryptedData": encryptedData,
            }

            if validated_data.record_id:
                payload["recordId"] = validated_data.record_id

            if validated_data.public_key:
                payload["publicKey"] = validated_data.public_key

            fhir_bundle_response: FhirBundleResponse = await self.post(
                AI_ENDPOINTS.GENERATE_FHIR_BUNDLE,
                payload,
                response_model=FhirBundleResponse,
            )

            return fhir_bundle_response.root

        except EhrApiError as e:
            self.logger.error(
                f"EHR API Error during FHIR bundle generation: {e.message}",
                exc_info=True,
            )
            raise
        except ValueError as e:
            self.logger.error(
                f"Validation error in FHIR bundle generation: {e}", exc_info=True
            )
            raise EhrApiError(str(e), 422) from e
        except Exception as error:
            error_message = str(error)
            self.logger.error(
                f"Unexpected error in generate_fhir_bundle: {error_message}",
                exc_info=True,
            )
            raise EhrApiError(
                "An unexpected error occurred while generating FHIR bundle: "
                f"{error_message}",
                500,
            ) from error
        

    async def generate_discharge_summary(self, process_data: dict[str, Any]) -> DischargeSummaryResponse:
        """
        Generate a discharge summary using AI based on the provided case data.

        This method validates and processes the input data, encrypts it if necessary, and calls the AI API
        to generate a discharge summary. Use this to automate the creation of discharge summaries from
        structured/unstructured clinical data.

        Args:
            process_data (dict[str, Any]): Dictionary containing required inputs such as case type, files,
                encryptedData, and publicKey.

        Returns:
            DischargeSummaryResponse: Contains:
                - dischargeSummary (Optional[dict]): AI-generated discharge summary content
                - extractedData (dict): Extracted structured clinical content
                - fhirBundle (dict): FHIR-compliant bundle based on extracted data

        Raises:
            ValueError: If both 'files' and 'encryptedData' are missing.
            ValidationError: If input fails schema validation.
            EhrApiError: Raised when the API returns error status codes (400, 422, 500).

        Example (Success):
            ```python
            response = await service.generate_discharge_summary({
                "files": ["file123.pdf"],
            })

            print(response.dischargeSummary["diagnosis"])
            ```

        Example (Validation Failure):
            ```python
            await service.generate_discharge_summary({
                "caseType": "DISCHARGE_SUMMARY"
            })
            # Raises EhrApiError: No files or encrypted data provided (422)
            ```
        """
        return await self.generate_case_summary(process_data, HealthInformationTypes.DISCHARGE_SUMMARY.value)


    async def generate_op_consultation_summary(self, process_data: dict[str, Any]) -> DischargeSummaryResponse:
        """
        Generate an OP consultation summary using AI based on the provided case data.

        This method validates and processes the input, encrypts it if necessary, and calls the AI API
        to generate an outpatient consultation summary.

        Args:
            process_data (dict[str, Any]): Dictionary containing required inputs such as case type, files,
                encryptedData, and publicKey.

        Returns:
            DischargeSummaryResponse: Contains:
                - dischargeSummary (Optional[dict]): AI-generated OP consultation summary
                - extractedData (dict): Extracted structured consultation data
                - fhirBundle (dict): FHIR-compliant bundle based on extracted data

        Raises:
            ValueError: If both 'files' and 'encryptedData' are missing.
            ValidationError: If input fails schema validation.
            EhrApiError: Raised when the API returns error status codes (400, 422, 500).

        Example:
            ```python
            response = await service.generate_op_consultation_summary({
                "files": ["consultation_notes.pdf"],
            })
            ```
        """
        return await self.generate_case_summary(process_data, HealthInformationTypes.OPCONSULTATION.value)


    async def generate_radiology_summary(
        self, process_data: dict[str, Any]
    ) -> RadiologySummaryResponse:
        """
        Generate a radiology/diagnostic report summary using AI.

        This method validates and processes radiology/diagnostic data,
        encrypts it if necessary, and calls the AI API to generate
        a diagnostic summary report.

        Args:
            process_data (dict[str, Any]): Dictionary containing required inputs
                such as files, encryptedData, and publicKey.

        Returns:
            DischargeSummaryResponse: Contains:
                - dischargeSummary (Optional[dict]): AI-generated radiology summary
                - extractedData (dict): Extracted structured diagnostic data
                - fhirBundle (dict): FHIR-compliant bundle based on extracted data

        Raises:
            ValueError: If both 'files' and 'encryptedData' are missing.
            EhrApiError: Raised when the API returns error status codes (400, 422, 500).
        """

        self.logger.info(f"Starting generation of radiology summary with data: {process_data}")

        try:
            process_dto: ProcessDSDto = await self._validate_data(ProcessDSDto, process_data)

            # Throw error if no encryptedData or files
            if not process_dto.encrypted_data and not process_dto.files:
                raise ValueError("No files or encrypted data provided.")

            # Use encryptedData if provided, else encrypt files
            if process_dto.encrypted_data:
                encrypted_data = process_dto.encrypted_data
            else:
                payload_to_encrypt = {"files": process_dto.files}
                encrypted_data = await self.utilities.encryption(payload=payload_to_encrypt)

            # Build payload
            payload = {
                "caseType": HealthInformationTypes.DIAGNOSTIC_REPORT.value,
                "encryptedData": encrypted_data,
            }
            if process_dto.public_key:
                payload["publicKey"] = process_dto.public_key
            
            response: RadiologySummaryResponse = await self.post(
                AI_ENDPOINTS.GENERATE_RADIOLOGY_SUMMARY,
                payload,
                response_model=RadiologySummaryResponse,
            )

            
            return response

            

        except EhrApiError as e:
            self.logger.error(f"EHR API Error during radiology summary generation: {e.message}", exc_info=True)
            raise
        except ValueError as e:
            self.logger.error(f"Validation error in radiology summary generation: {e}", exc_info=True)
            raise EhrApiError(str(e), 422) from e
        except Exception as error:
            error_message = str(error)
            self.logger.error(f"Unexpected error in radiology summary generation: {error_message}", exc_info=True)
            raise EhrApiError(
                f"An unexpected error occurred while generating radiology summary: {error_message}", 500
                ) from error

    async def partial_upload_for_discharge_summary(
        self, process_ds_dto: ProcessDSDto
    ) -> Dict[str, Any]:
        """
            Perform a partial upload for discharge summary generation.

            This method validates the provided data, performs encryption if necessary,
            constructs the appropriate payload, and makes an API call to trigger
            a partial discharge summary upload.

            Args:
                process_ds_dto (ProcessDSDto): DTO containing encounter details, files,
                    encryption data, and metadata required for the upload.

            Returns:
                Dict[str, Any]: The JSON response from the AI service after
                processing the partial upload.

            Raises:
                ValueError: If neither `encrypted_data` nor `files` are provided.
                EhrApiError: If an error occurs during encryption or the API call.

            Example:
                >>> dto = ProcessDSDto(
                ...     encounter_id="enc-12345"(not required for first time),
                ...     files=[{"file1": "lab_report.pdf", "file2": "..."}],
                ...     date=2025-10-01T10:00:00Z,
                ... )
                >>> result = await ai_service.partial_upload_for_discharge_summary(dto)
                >>> print(result)
                {
                "id": "0c4cce09-b7bd-4255-8182-b2c3586ere001c9",
                "dischargeSummary": {},
                "extractedData": {
                    "Patient Details": {
                        "Name": "Mr. Sri Ram",
                        "Age": "16 Year(s) 6 Month(s)",
                        "Sex": "Male",
                        .....
                        }   
                    },
                }
        """


        # Validate input
        process_dto: ProcessDSDto = await self._validate_data(ProcessDSDto, process_ds_dto)

        if not process_dto.encrypted_data and not process_dto.files:
            raise ValueError("No files or encrypted data provided.",422)

        # Either use encrypted_data or perform encryption
        if process_dto.encrypted_data:
            encrypted_data = process_dto.encrypted_data
        else:
            payload_to_encrypt = {"files": process_dto.files}
            encrypted_data = await self.utilities.encryption(
                payload=payload_to_encrypt, public_key=process_dto.public_key
            )

        # Build payload
        payload: Dict[str, Any] = {
            "caseType": HealthInformationTypes.DISCHARGE_SUMMARY.value,
            "uploadMode": "Partial",
            "date": process_dto.date
            or datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
            "encounterId": process_dto.encounter_id,
            "encryptedData": encrypted_data,
        }

        if process_dto.public_key:
            payload["publicKey"] = process_dto.public_key

        # Call API
        try:
            response = await self.post(
                AI_ENDPOINTS.GENERATE_DISCHARGE_SUMMARY,
                payload,
                response_model=dict,
            )
            return response
        except EhrApiError as e:
            self.logger.error(
                f"EHR API Error during Partial upload for discharge summary generation: {e.message}",
                exc_info=True,
            )
            raise
        except ValueError as e:
            self.logger.error(
                f"Validation error in Partial upload for discharge summary generation: {e}", exc_info=True
            )
            raise EhrApiError(str(e), 422) from e
        except Exception as error:
            error_message = str(error)
            self.logger.error(
                f"Unexpected error in Partial upload for discharge summary generation: {error_message}",
                exc_info=True,
            )
            raise EhrApiError(
                "An unexpected error occurred while Partial upload for discharge summary generation: "
                f"{error_message}",
                500,
            ) from error

    async def trigger_discharge_summary(self, encounter_id: str) -> Any:
        """
            Trigger discharge summary generation for a given encounter ID.

            This method sends a PUT request to the AI service endpoint to initiate
            discharge summary generation for the specified encounter. It ensures the
            `encounter_id` is valid before making the request.

            Args:
                encounter_id (str): The unique identifier of the encounter.
                    Must be a non-empty string.

            Returns:
                Dict[str, Any]: The JSON response from the AI service containing
                the status of the discharge summary generation.

            Raises:
                ValueError: If `encounter_id` is missing or blank.
                EhrApiError: If an error occurs during the API request.

            Example:
                >>> result = await ai_service.trigger_discharge_summary("enc-12345")
                >>> print(result)
                {
                    "data": "{\n  \"patientDetails\": {\n    \"Name\": \"Mr. Sri Ram\",\n    \"Age\": \"16 years 6 months\",\n    \"Gender\": \"Male\",\n.........."}",
                    "message": "Discharge for record enc-12345 generated successfully"
                }
        """
        if not encounter_id or not encounter_id.strip():
            raise ValueError("Encounter ID must not be blank.")

        payload: Dict[str, Any] = {"updateType": "Generate Discharge"}
        url = f"{AI_ENDPOINTS.UPDATE_DISCHARGE_SUMMARY_URL}/{encounter_id}"

        try:
            response = await self.put(url, payload, response_model=dict)
            return response
        except EhrApiError:
            raise
        except Exception as error:
            error_message = str(error)
            self.logger.error(
                f"Unexpected error in trigger_discharge_summary for encounterId={encounter_id}: {error_message}",
                exc_info=True,
            )
            raise EhrApiError(
                f"An unexpected error occurred while triggering discharge summary for encounterId={encounter_id}: {error_message}",
                500,
            ) from error

    async def generate_careplan(self, process_ds_dto: ProcessDSDto) -> Dict[str, Any]:
        """
            Generate a patient care plan from provided files or encrypted data.

            This method validates the input data, encrypts it if required, and sends the
            payload to the AI service endpoint for care plan generation. It handles
            validation errors, encryption failures, and unexpected errors gracefully.

            Args:
                process_ds_dto (ProcessDSDto):
                    The input DTO containing files, encrypted data, and optional encryption keys.

            Returns:
                Dict[str, Any]: 
                    A dictionary containing the AI-generated care plan response.

            Raises:
                EhrApiError: If the API call fails (status code 500)
                ValueError: Raised internally for missing `files` or `encrypted_data` before being
                    wrapped as an `EhrApiError`.

            Example Input if files are provided:
                >>> dto = ProcessDSDto(
                ...     files=["file1.pdf", "file2.pdf"],
                ... )
                >>> response = await ai_service.generate_careplan(dto)

            Example Input if encrypted data is provided:
                >>> dto = ProcessDSDto(
                ...     encrypted_data="encrypted_payload_string",
                ...     public_key="-----BEGIN PUBLIC KEY-----\n...\n-----END PUBLIC KEY-----"
                ... ) response = await ai_service.generate_careplan(dto)

            Example Output:
                {
                    "id": "a1956730-546534265f-4c2d-8902-a34fe3645886b24",
                    "carePlan": {
                        "patientDetails": {
                            "name": "Ram sai",
                            "age": "75Y(s) 6M(s) 30D(s)",
                            "sex": "Male",
                            "uhid": "MRKO252643654325015739",
                            "visitId": "IPKO243534005789",
                            "address": "Mumbai",
                            "contactNumber": "9876543210"
                        },
                        "doctorDetails": [
                            {
                                "name": "DR. BALAKRISHNA N",
                                "designation": "MBBS, MD, DM (Cardiology), Sr. Consultant Cardiologist.",
                                "department": "CARDIOLOGY"
                            },
                            {
                                "name": "DR. SHYAM SINGA ROY. G",
                                "designation": "MBBS, MD (General Medicine), DM (Neurology), Consultant Neurologist",
                                "department": "NEUROLOGY"
                            }
                        ],
                        ....
                    }
                }

        """
        try: 
            process_dto: ProcessDSDto = await self._validate_data(ProcessDSDto, process_ds_dto)

            if not process_dto.encrypted_data and not process_dto.files:
                raise ValueError("No files or encrypted data provided.")

            if process_dto.encrypted_data:
                encrypted_data = process_dto.encrypted_data
            else:
                payload_to_encrypt = {"files": process_dto.files}
                encrypted_data = await self.utilities.encryption(
                    payload=payload_to_encrypt, public_key=process_dto.public_key
                )

            payload: Dict[str, Any] = {"encryptedData": encrypted_data}
            if process_dto.public_key:
                payload["publicKey"] = process_dto.public_key

            response = await self.post(
                AI_ENDPOINTS.GENERATE_CAREPLAN,
                payload,
                response_model=dict,
            )

            if not isinstance(response, dict):
                raise EhrApiError("Invalid response format from care plan API.", 502)
            
            return response

        except EhrApiError as e:
            self.logger.error(f"EHR API Error during care plan generation: {e.message}", exc_info=True)
            raise
        except ValueError as e:
            self.logger.error(f"Validation error in care plan generation: {e}", exc_info=True)
            raise EhrApiError(str(e), 422) from e
        except Exception as error:
            error_message = str(error)
            self.logger.error(f"Unexpected error while generating care plan: {error_message}", exc_info=True)
            raise EhrApiError(
                f"An unexpected error occurred while generating care plan: {error_message}",
                500,
            ) from error
