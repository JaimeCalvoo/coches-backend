from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
import base64
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/scan")
async def scan_car(file: UploadFile = File(...)):
    image_bytes = await file.read()

    # Convertimos la imagen a base64
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Identifica la marca y modelo exacto del coche en esta imagen. Responde solo con: Marca - Modelo"
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{image_base64}"
                    }
                ]
            }
        ]
    )

    return JSONResponse(content={
        "detected": response.output_text
    })
