import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline

# Inicializar la aplicación FastAPI
app = FastAPI(
    title='AI Services with TinyLlama',
    description='API para interactuar con TinyLlama',
    version='1.0.0'
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuración del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializar el pipeline de TinyLlama
pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    torch_dtype=torch.bfloat16,
    device_map="cpu"
)

# Definir la ruta principal de la API
@app.get("/")
async def read_root():
    return {"message": "Bienvenido a la API de TinyLlama"}

# Definir la ruta para generar texto con TinyLlama
@app.post("/generate")
async def generate_text(prompt: str):
    try:
        # Configuración del prompt para TinyLlama
        messages = [
            {"role": "system", "content": "You are a friendly chatbot."},
            {"role": "user", "content": prompt},
        ]
        # Obtener el texto generado por TinyLlama
        prompt_text = pipe.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        outputs = pipe(
            prompt_text,
            max_new_tokens=256,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
        )
        # Devolver el texto generado
        return {"generated_text": outputs[0]["generated_text"]}
    except Exception as e:
        logger.error(f"Error generando texto: {e}")
        raise HTTPException(status_code=500, detail="Error generando texto")

# Mensaje al iniciar la aplicación
@app.on_event("startup")
async def startup_event():
    logger.info("API de TinyLlama iniciada")
