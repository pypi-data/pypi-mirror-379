# CastleGuard Python SDK

The CastleGuard Python SDK provides a convenient interface to interact with CastleGuard's API. This SDK allows you to authenticate, log messages, interact with the chatbot, translate text, perform named entity recognition (NER), transcribe audio files, manage document collections, work with vision-based models, and more.

## Features

- **Authentication**: Easily authenticate and retrieve an access token to interact with CastleGuard APIs.
- **Logging**: Send log messages to CastleGuard's logging endpoint.
- **Chatbot Integration**: Interact with CastleGuard's chatbot to generate responses based on input prompts, with or without document collections.
- **Translation**: Translate text between languages, supporting English and French.
- **Named Entity Recognition (NER)**: Perform NER on text to extract important entities.
- **Vision**: Perform image-based tasks using a vision model by uploading an image with a descriptive prompt.
- **Transcription**: Upload and transcribe audio files, and download SRT subtitles.
- **Collections**: Manage document collections by creating, uploading, and retrieving the status of files.
- **Heartbeat**: Fetch the health status of various system components.
- **Text Extraction**: Extract paragraphs from raw text or extract text from a document file.

## Installation

Install the package via pip:

```bash
pip install castleguard-sdk
```

## Usage

### Initialization

To begin, initialize the `CastleGuard` class with your API credentials:

```python
from castleguard_sdk import CastleGuard

cg = CastleGuard(base_url='https://your-castleguard-url', username='your-username', password='your-password')
```

### Authentication

The class automatically handles authentication. The access token is retrieved upon initialization and used for subsequent API requests.

### Logging

Log a message with a specific log level (default is 1):

```python
cg.log("This is a log message", logLevel=2)
```

### Chatbot Interaction

Send a prompt to the chatbot and get a response:

```python
response, chat_id = cg.chat("What is the weather today?")
print(response)
```

You can also chat within the context of a document collection:

```python
response, chat_id = cg.chat_with_collection("Summarize the document", collection_id="your-collection-id")
print(response)
```

### Translation

### 1. Instant Text Translation
Translate a single text with `translate_text`:

```python
translated_text = cg.translate_text("Hello, how are you?", source_lang="en", target_lang="fr")
print(translated_text)
```

#### Parameters
- **text**: The text string to be translated.
- **source_lang**: Source language code.
- **target_lang**: Target language code.

#### Returns
- The translated text. Returns `None` if an error occurs.

### 2. Multiple Text Translations
Translate multiple texts simultaneously with `translate_texts`:

```python
texts = ["Hello", "Goodbye"]
source_langs = ["en", "eng"]
target_langs = ["fr", "deu"]
translated_texts = cg.translate_texts(texts, source_langs, target_langs)
print(translated_texts)
```

#### Parameters
- **texts**: List of text strings to translate.
- **source_langs**: List of source language codes, one for each text.
- **target_langs**: List of target language codes, one for each text.

#### Returns
- A list of dictionaries, where each dictionary contains:
  - **originalText**: The original text provided.
  - **translatedText**: The translated text.
  - **sourceLanguageCode**: The source language code.
  - **targetLanguageCode**: The target language code.
  
  Returns `None` if an error occurs.


**Note**: The lists for `texts`, `source_langs`, and `target_langs` must be of equal length.

### 3. Document Translation
Upload an audio file and translate it:

```python
document_id = cg.translate_document("path/to/file", source_lang="en", target_lang="fr")
print(f"Document ID: {document_id}")
```

#### Parameters
- **file_path**: Path to the file to be translated. This path can be relative to the file where this function is called (e.g., `.` or `../`) or an absolute path.
- **source_lang**: Source language code.
- **target_lang**: Target language code.
- **keep_original**: Whether to retain the original document (default is True).

#### Returns
- A `document_id` for the created document. `None` if an error occurs.

### 4. Translate Multiple Documents
Translate multiple documents:

```python
file_paths = ["/path/tofile1.txt", "/path/tofile2.docx"]
document_ids = cg.translate_documents(file_paths, source_lang="en", target_lang="fr")
print(f"Document IDs: {document_ids}")
```
#### Parameters
- **file_path_list**: List of file paths to be translated. Like the single-file method, each path can be relative to the file where this function is called (e.g., `.` or `../`) or an absolute path.

- **source_lang**: Source language code.
- **target_lang**: Target language code.
- **keep_original**: Whether to retain the original document (default is True).
### Returns

The function returns a list of dictionaries, each corresponding to a document. Each dictionary contains the following keys:

- **`document_id`**: A unique identifier for the document.
- **`status`**: The outcome of the translation, either `"fail"` or `"success"`.
- **`status_code`**: A numerical status code (e.g., `2` for finished).
- **`status_name`**: A descriptive status name (e.g., `"finished"`).

In case of an error, the function will return `None`.


### 5. Downloading Documents
#### Original Document
```python
saved_original_path = cg.download_translation_original(document_id, save_path="./downloads", file_name="original_file.txt")
```

#### Translated Document
```python
saved_translated_path = cg.download_translation_translated(document_id, save_path="./downloads", file_name="translated_file.txt")
```

#### Parameters
- **document_id**: The ID of the document.
- **save_path**: The path where the document will be saved. This can be either a relative path (e.g., `.` or `../`) or an absolute path. If not provided, the file will be saved in the current working directory by default.
- **file_name**: The name of the file to save the document as. If not provided, the default file name will be auto-generated based on the original file name, source and target languages, and document type (e.g., 'original' or 'translated').

#### Returns
- The **path** where the document will be saved. If any error occurs, it will return `None`.
### 6. Get Translation Document Status

#### Single Document
Check the status of a single document:

```python
status_code = cg.get_translation_document_status(document_id)
print(status_code)
```

#### Parameters
- **document_id**: The ID of the document.

#### Returns
- The **status code** (e.g., "success", "failed") if successful, `None` if an error occurs.

#### Multiple Documents
Check the status of multiple documents at once:

```python
document_ids = [document_id1, document_id2]
statuses = cg.get_translation_documents_status(document_ids)
print(statuses)
```

#### Parameters
- **document_ids**: A list of document IDs to check the status for.

#### Returns
- A **list of dictionaries**, each containing:
  - `"document_id"`: Unique identifier for the document.
  - `"status"`: Translation outcome, either `"fail"` or `"success"`.
  - `"status_code"`: Numerical status code (e.g., `2` for finished, `0` for queued).
  - `"status_name"`: Status description (e.g., `"finished"`, `"queued"`).
- In case of an error, the function will return `None`.

### Named Entity Recognition (NER)

Perform NER on text to extract entities:

### 2. Process Text
```python
entities = cg.named_entity_recognition("John Doe works at Google in Mountain View.")
print(entities)
```
#### Parameters
- **text**: The input text for performing NER. The function will analyze the provided text to identify entities such as names, locations, dates, and other key terms.

#### Returns
- A dictionary containing the original text and a list of extracted entities. The entities are structured as dictionaries with:
  - `entityType`: The type of entity (e.g., "PERSON", "GPE", "DATE", "ORG").
  - `value`: The actual entity extracted from the text.
  - `startPosition`: The start index of the entity in the text.
  - `endPosition`: The end index of the entity in the text.

#### Process Multiple Texts
To process multiple texts at once:

```python
texts = ["John Doe works at Google.", "Jane Smith is a doctor in New York."]
entities_list = cg.named_entity_recognition_multiple_text(texts)
print(entities_list)
```

#### Parameters
- **text_list**: A list of input texts for performing NER on multiple documents.

#### Returns
- A list of dictionaries, where each dictionary contains:
  - The `text` field with the original text.
  - The `entities` field, which is a list of extracted entities for that text.
  
### Vision

Upload an image file and provide a descriptive prompt to perform vision-based tasks:

```python
vision_result = cg.vision(prompt="Detect objects in this image", file_path="/path/to/image.jpg")
print(vision_result)
```

### Transcription

#### 1. Document Translation
Upload an audio file and transcribe it:

```python
document_id = cg.transcribe("/path/to/audiofile.mp3")
```

#### Parameters
- **file_path**: Path to the audio file to transcribe. This path can be relative to the file where this function is called (e.g., `.` or `../`) or an absolute path.
- **diarization_config**: (Optional) Diarization configuration. Default is 1.

#### Returns
- A `document_id` for the created document. `None` if an error occurs.


#### 2. Transcribe Multiple Documents
Transcribe multiple documents:

```python
file_paths = ["/path/to/audiofile1.mp3", "/path/to/audiofile2.mp3"]
transcription_status = cg.transcribe_multiple(file_paths)
print(transcription_status)
```

#### Parameters
- **file_path_list**: List of paths to the audio files to transcribe. Like the single-file method, each path can be relative to the file where this function is called (e.g., `.` or `../`) or an absolute path.

- **diarization_config**: (Optional) Diarization configuration. Default is 1.

### Returns

The function returns a list of dictionaries, each corresponding to a document. Each dictionary contains the following keys:

- **`document_id`**: A unique identifier for the document.
- **`status`**: The outcome of the translation, either `"fail"` or `"success"`.
- **`status_code`**: A numerical status code (e.g., `2` for finished).
- **`status_name`**: A descriptive status name (e.g., `"finished"`).

In case of an error, the function will return `None`.

#### 3. Downloading Documents
#### Original Document
```python
saved_file_path = cg.download_transcription_original_file(document_id, save_path="./transcriptions")
```

#### SRT Document
```python
saved_srt_path = cg.download_srt_file(document_id, save_path="./subtitles")
```

#### Transcription Document
```python
transcription_text_path = cg.download_transcription_file(document_id, save_path="./transcriptions")
```

#### Parameters
- **document_id**: The ID of the document.
- **save_path**: The path where the document will be saved. This can be either a relative path (e.g., `.` or `../`) or an absolute path. If not provided, the file will be saved in the current working directory by default.
- **file_name**: Name for the saved file. If not provided, it will be auto-generated based on the original file name and document type (e.g., 'original' or 'SRT').

#### Returns
- The **path** where the document will be saved. If any error occurs, it will return `None`.

#### 4. Download SRT Text Directly
To download the SRT text directly without saving it to a file, use `download_srt`:

```python
srt_text = cg.download_srt(document_id)
print(srt_text)
```

#### Parameters
- **document_id**: The ID of the transcription document.

#### Returns
- The **SRT text** if successful, `None` if an error occurs.


#### 5. Get Transcription Document Status

#### Single Document
Check the status of a single document:

```python
status_code = cg.get_transcription_document_status(document_id)
print(status_code)
```

#### Parameters
- **document_id**: The ID of the document.

#### Returns
- The **status code** (e.g., "success", "failed") if successful, `None` if an error occurs.

#### Multiple Documents
Check the status of multiple documents at once:


```python
document_ids = [document_id1, document_id2]
statuses = cg.get_transcription_documents_status(document_ids)
print(statuses)
```

#### Parameters
- **document_ids**: A list of document IDs to check the status for.

#### Returns
- A **list of dictionaries**, each containing:
  - `"document_id"`: Unique identifier for the document.
  - `"status"`: Translation outcome, either `"fail"` or `"success"`.
  - `"status_code"`: Numerical status code (e.g., `2` for finished, `0` for queued).
  - `"status_name"`: Status description (e.g., `"finished"`, `"queued"`).
- In case of an error, the function will return `None`.

### Anonymizer

#### 1. Anonymize Document
Upload an file and anonymize it:

```python
document_id = cg.anonymize_document(
    '/path/to/file1.txt',
    [EntityType.ADDRESS.value],
)
```

#### Parameters
- **file_path**: Path to the file to anonymize. This path can be relative to the file where this function is called (e.g., `.` or `../`) or an absolute path.
- **options**: List of `EntityType` values to anonymize. If not provided, no entity-based anonymization will be performed.
- **regex**: Regular expression to match and anonymize additional custom data. If not provided, no regex-based anonymization will be performed.
#### Returns
- A `document_id` for the created document. `None` if an error occurs.

#### 2. Anonymize Multiple Documents
Anonymize multiple documents:
```python
documents_status = cg.anonymize_documents(
    ['/path/to/file1.txt', '/path/to/file2.txt',],
    [EntityType.PERSON.value, EntityType.WORK_OF_ART.value],
    "\\b2019\\b"
)

```

#### Parameters
- **file_path_list**: List of paths to the files to anonymize. Like the single-file method, each path can be relative to the file where this function is called (e.g., `.` or `../`) or an absolute path.
- **options**: List of `EntityType` values to anonymize. If not provided, no entity-based anonymization will be performed.
- **regex**: Regular expression to match and anonymize additional custom data. If not provided, no regex-based anonymization will be performed.
### Returns

The function returns a list of dictionaries, each corresponding to a document. Each dictionary contains the following keys:

- **`document_id`**: A unique identifier for the document.
- **`status`**: The outcome of the translation, either `"fail"` or `"success"`.
- **`status_code`**: A numerical status code (e.g., `2` for finished).
- **`status_name`**: A descriptive status name (e.g., `"finished"`).

In case of an error, the function will return `None`.

### Entity Types for Anonymization
The following `EntityType` values are available for anonymization. You can specify a list of these entities when calling the anonymization methods:

```python
EntityType.ADDRESS
EntityType.CARDINAL
EntityType.COMPANY
EntityType.CRYPTO
EntityType.DATE
EntityType.DNS
EntityType.EMAIL
EntityType.EVENT
EntityType.FAC
EntityType.GPE
EntityType.IP
EntityType.LANGUAGE
EntityType.LAW
EntityType.LOC
EntityType.MONEY
EntityType.NORP
EntityType.ORDINAL
EntityType.ORG
EntityType.PERCENT
EntityType.PERSON
EntityType.PHONE
EntityType.PRODUCT
EntityType.QUANTITY
EntityType.TIME
EntityType.WORK_OF_ART
```

#### 3. Downloading Documents
#### Original Document
```python
saved_file_path = cg.download_anonymized_original_documnet(document_id, save_path="./downloads",file_name="original")
```
#### Anonymized Document
```python
saved_srt_path = cg.download_anonymized_documnet(document_id, save_path="./subtitles",file_name="original")
```

#### Parameters
- **document_id**: The ID of the document.
- **save_path**: The path where the document will be saved. This can be either a relative path (e.g., `.` or `../`) or an absolute path. If not provided, the file will be saved in the current working directory by default.
- **file_name**: Name for the saved file. If not provided, it will be auto-generated based on the original file name and document type (e.g., 'original' or 'anonymized').

#### Returns
- The **path** where the document will be saved. If any error occurs, it will return `None`.

#### 5. Get Anonymized Document Status

#### Single Document
Check the status of a single document:


```python
document_status = cg.get_anonymized_document_status(document_id)
print(document_status)
```

#### Parameters
- **document_id**: The ID of the document.

#### Returns
- The **status code** (e.g., "success", "failed") if successful, `None` if an error occurs.

#### Multiple Documents
Check the status of multiple documents at once:


```python
document_ids = [document_id1, document_id2]
statuses = cg.get_anonymized_documents_status(document_ids)
print(statuses)
```

#### Parameters
- **document_ids**: A list of document IDs to check the status for.

#### Returns
- A **list of dictionaries**, each containing:
  - `"document_id"`: Unique identifier for the document.
  - `"status"`: Translation outcome, either `"fail"` or `"success"`.
  - `"status_code"`: Numerical status code (e.g., `2` for finished, `0` for queued).
  - `"status_name"`: Status description (e.g., `"finished"`, `"queued"`).
- In case of an error, the function will return `None`.


### Document Collections

Create a new document collection:

```python
collection_id = cg.create_collection(name="My Collection", description="A collection of legal documents")
print(f"Collection created with ID: {collection_id}")
```

Upload a document to the collection:

```python
upload_success = cg.upload_to_collection(collection_id, "/path/to/document.pdf")
print(f"Upload successful: {upload_success}")
```

### Heartbeat

Fetch the health status of various system components:

```python
heartbeat_status = cg.heartbeat()
print(heartbeat_status)
```

##### Parameters:
- None

##### Returns:
- **Dictionary**: A dictionary with the status of each component. Each key represents a system component (e.g., `"SQL Server"`, `"Oracle DB"`) and contains the following fields:
  - **status**: The health status of the component, typically `"UP"` or `"DOWN"`.
  - **message**: A message providing more details about the component's health.
  - **sinceTimestamp**: A timestamp indicating when the status was last updated.



```python
health_status = cg.healthcheck()
print(health_status)
```

#### Parameters:
- None

#### Returns:
- **List of Tuples**: The returned list contains tuples where each tuple represents a system resource and its health status. Each tuple contains:
  - **resource name**: The name of the resource (e.g., `"SQL Server"`, `"Oracle DB"`, `"Training GRPC"`, `"Triton Grpc Server"`).
  - **status**: The health status of the resource, which can be either `"UP"` (healthy) or `"DOWN"` (unhealthy).
  
#### Example Response Structure:
```python
[
  ("SQL Server", "UP"),
  ("Oracle DB", "UP"),
  ("Training GRPC", "DOWN"),
  ("Triton Grpc Server", "UP")
]
```


### Text Extraction

Extract paragraphs from raw text:

```python
paragraphs = cg.text_extraction("This is a sample text that needs to be divided into paragraphs.")
print(paragraphs)
```

Extract text from a document file:

```python
extracted_text = cg.text_extraction_from_document("/path/to/document.pdf")
print(extracted_text)
```


### Text Embedding

Generate embeddings from raw text:

```python
result = cg.get_text_embedding("This is a sample text.")
print(result)
```


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.