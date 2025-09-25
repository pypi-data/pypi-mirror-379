import json
import re
import os
from google.oauth2 import service_account
from google.cloud import vision
from google.cloud import storage

import sys


class DetectTextInFiles:
    def __init__(self,gcs_source_uri,gcs_destination_uri,credentials_path,batch_size):
        self.gcs_source_uri = gcs_source_uri
        self.gcs_destination_uri = gcs_destination_uri
        self.credentials_path=credentials_path
        self.batch_size=batch_size
        try:
            self.credentials = service_account.Credentials.from_service_account_file(self.credentials_path)
            # Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
            # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.credentials_path
            print("Authenticated successfully using service account key.")
        except Exception as e:
            print(f"Authentication failed using service account key: {e}")

    def async_detect_document(self):
        """OCR with PDF/TIFF as source files on GCS"""

        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

        # Supported mime_types are: 'application/pdf' and 'image/tiff'
        mime_type = "application/pdf"

        # How many pages should be grouped into each json output file.
        batch_size = self.batch_size

        client = vision.ImageAnnotatorClient()

        feature = vision.Feature(type_=vision.Feature.Type.DOCUMENT_TEXT_DETECTION)

        gcs_source = vision.GcsSource(uri=self.gcs_source_uri)
        input_config = vision.InputConfig(gcs_source=gcs_source, mime_type=mime_type)

        gcs_destination = vision.GcsDestination(uri=self.gcs_destination_uri)
        output_config = vision.OutputConfig(
            gcs_destination=gcs_destination, batch_size=batch_size
        )

        async_request = vision.AsyncAnnotateFileRequest(
            features=[feature], input_config=input_config, output_config=output_config
        )

        operation = client.async_batch_annotate_files(requests=[async_request])

        print("Waiting for the operation to finish.")
        operation.result(timeout=420)

        # Once the request has completed and the output has been
        # written to GCS, we can list all the output files.
        storage_client = storage.Client()

        match = re.match(r"gs://([^/]+)/(.+)", self.gcs_destination_uri)
        bucket_name = match.group(1)
        prefix = match.group(2)

        bucket = storage_client.get_bucket(bucket_name)

        # List objects with the given prefix, filtering out folders.
        # blob_list = [
        #     blob
        #     for blob in list(bucket.list_blobs(prefix=prefix))
        #     if not blob.name.endswith("/")
        # ]
        blob_list = list(bucket.list_blobs(prefix=prefix))
        print("Output files:")
        for blob in blob_list:
            print(blob.name)

        # Process the first output file from GCS.
        # Since we specified batch_size=2, the first response contains
        # the first two pages of the input file.
        for  n in range(len(blob_list)):
            output = blob_list[n]

            # json_string = output.download_as_bytes().decode("utf-8")
            json_string = output.download_as_string()
            response = json.loads(json_string)

            file=open("output_{}.txt".format(str(n)),"w", encoding="utf-8")

            # The actual response for the first page of the input file.
            for m in range(len(response["responses"])):
                first_page_response = response["responses"][m]
                annotation = first_page_response["fullTextAnnotation"]

                # Here we print the full text from the first page.
                # The response contains more information:
                # annotation/pages/blocks/paragraphs/words/symbols
                # including confidence scores and bounding boxes
                print("Full text:\n")
                try:
                    print(annotation["text"])
                except UnicodeEncodeError:
                    print(
                        annotation["text"].encode(
                            sys.stdout.encoding or "utf-8", errors="replace"
                        ).decode(sys.stdout.encoding or "utf-8")
                    )
                file.write(annotation["text"])

# if __name__ == "__main__":
#     detect_text_in_files = DetectTextInFiles(
#         gcs_source_uri="gs://vidur-vision-api-test/6  ITC 439.pdf",
#         gcs_destination_uri="gs://vidur-vision-api-test/6  ITC 439.json",
#         credentials_path="C:/easy_utility/gemini-api-key-sum-c69f57721f71.json",
#         batch_size=100
#     )
#     detect_text_in_files.async_detect_document()