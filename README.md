# StegAPI

A secure stegnography-based Rest API that allows user to hide their message inside PNG images using (LSB) encoding

---

## Example

#hello_i_am_yogesh : Encrypted inside image ... : Looks normal ...Sent to the Person

Person comes to Website ..Uploads Image ...Boom ...hello_i_am_yogesh message is decoded :) *(Used In Cybersecurity)*

---

## OverView Of the Project

Its a cybersec and Image processing API built using FastAPI .....

Api helps user to :

- encode their message in the PNG image  
- Decode hidden Message from Images  
- Encrypt text using XOR encryption  
- Track API activity (JSON logging)  

---

## What this Project Taught me

- Stegnography  
- Cryptography (Encoding/Decoding)  
- Image_Processing  
- Backend (Database we Can Say)  
- And Then manythings About API  

---

## Why I built it

Because I had interest in Cybersec ,,and This Topic amazed me .)

---

## Tech stack

| Technology | Purpose |
|------------|---------|
| Python | Backend language |
| FastAPI | API framework |
| Uvicorn | ASGI server |
| Pillow (PIL) | Image processing |
| SlowAPI | Rate limiting |
| JSON | Persistence logging |

---

## Project Structure


StegAPI/
│
├── main.py
│
├── routers/
│ ├── encode.py
│ ├── decode.py
│ └── utility.py
│
├── utils/
│ ├── steg.py
│ └── security.py
│
├── uploads/
├── encoded/
├── logs/
│ └── history.json
│
├── README.md
└── pyproject.toml


---

## How The LSB works

LSB (Least Significant Bit) steganography hides binary data inside image pixels.

Each Pixel has some RGB value  
like : `10100101`

The last bit can be Modified Slightly :  
like : `10100100`

This tiny change Impossibe for Humans to Notice and it hides encrypted binary data inside the least significant bits of PNG image pixels.

---

## XOR Encryption

Before embedding the message into the image, the message is encrypted using XOR encryption.

this adds extra security layer before the hidden data is stored inside the image

The formula :


EncryptedCharacter = Character XOR Key


---

## Auth Section

Protected endpoints needs API

Header:


x-api-key


DEMO API KEY :


stegapi-secret-key


---

## Rate Limiting

The API uses SlowApi in the middle to avoid spams and all the abuse (API PROTECTION ENABLED ._.)

THE Limit is :


5 requests per minute .)


---

## Installation

Clone the repo


git clone 
cd stepapi


Install the dependencies :


uv add fastapi uvicorn pillow slowapi python-multipart


Then Start the Server :


uv run main.py


Then The API will run on :


http://127.0.0.1:8000/docs


---

## How to Use it

When clicking This 
http://127.0.0.1:8000/docs

You will see a Button to authorize..When Clicking it..U will enter the APi key

Then after authorizing ...U will click /encode and Click try it out...Then u will enter a (PNG PHOTO...OTHER PHOTO WON'T WORK) talking about format /.....and then Will write your message and execute ..after that you will download the file ...

MESSAGE ENCODED SUCCESSFULLY IN THE IMAGE

Then The Decoding

you will go to /decode...put the encoded image in it ...and execute ..in the 200 response..U can see the decoded message .... .)
Message Decoded Successfully .....

## The API docs in this :

Swagger Docs :


/docs


---

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Root endpoint |
| GET | /health | API health check |
| GET | /methods | List implemented techniques |
| GET | /binary | Binary conversion example |
| GET | /stats | View API logs |
| POST | /encode | Hide message inside image |
| POST | /decode | Extract hidden message |
| POST | /capacity | Calculate image capacity |
| POST | /image-info | Get image metadata |

---

## Example - Encode

POST /encode

Input:
- PNG image  
- Secret message  

Example Response:

```json
{
    "message": "Secret Message Encoded Successfully",
    "encoded_image": "encoded/encoded_image.png"
}
Example - Decode

POST /decode

Example Response:

{
    "decoded_message": "alpha"
}
Logging System

StegAPI stores operation history inside:

logs/history.json

The logs track:

Encode operations
Decode operations
Filenames
Timestamps
Why PNG Only

PNG images use lossless compression.

Formats like JPEG compress image data and destroy hidden binary information, making steganography unreliable.

Because of this, StegAPI only supports PNG images.