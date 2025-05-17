
import spacy

nlp = spacy.load("es_core_news_sm")

# chatbot_logica.py

RESPONSES = {
    "saludo": "¡Hola! Bienvenido a Honda Express. ¿En qué puedo ayudarte hoy?",
    "consulta_modelos": "Tenemos varios modelos Honda disponibles: Civic, CR-V, Accord y Fit. ¿Quieres detalles de algún modelo en particular?",
    "prueba_manejo": "Claro, puedes agendar tu prueba de manejo llamando al 55-1234-5678 o enviando un WhatsApp al mismo número. ¿Quieres que te ayude con la cita?",
    "financiamiento": "Ofrecemos planes de financiamiento flexibles y a tu medida. ¿Quieres que te explique las opciones?",
    "reclamo_tecnico": "Lamento que tengas problemas con tu vehículo. Por favor, describe la falla para ayudarte mejor.",
    "horarios_sucursal": "Nuestras sucursales están abiertas de lunes a sábado, de 9 am a 7 pm. ¿Quieres la dirección de alguna sucursal en especial?",
    "promociones": "Actualmente tenemos descuentos y promociones especiales en varios modelos Honda. ¿Quieres más información?",
    "confirmar_cita": "Por favor, proporciona tu número de cita o contrato para confirmar tu reservación.",
    "despedida": "Gracias por contactarnos en Honda Express. ¡Que tengas un excelente día!",
    "agradecimiento": "¡Con gusto! Si necesitas algo más, estoy aquí para ayudarte.",
    "unknown": "Disculpa, no entendí bien tu mensaje. ¿Puedes reformularlo o darme más detalles?"
}

INTENT_KEYWORDS = {
    "saludo": ["hola", "buenos días", "buenas tardes", "hey", "saludos"],
    "consulta_modelos": ["modelo", "modelos", "carro", "vehículo", "honda", "civic", "cr-v", "accord", "fit", "información", "precio"],
    "prueba_manejo": ["prueba de manejo", "test drive", "cita", "agendar", "reservar", "agenda", "llamar", "contacto"],
    "financiamiento": ["financiamiento", "crédito", "pago", "cuota", "plan", "mensualidad"],
    "reclamo_tecnico": ["problema", "falla", "avería", "reclamo", "reparación", "garantía"],
    "horarios_sucursal": ["horario", "sucursal", "ubicación", "dirección", "abierto", "cierre"],
    "promociones": ["promoción", "descuento", "oferta", "rebaja"],
    "confirmar_cita": ["confirmar", "cita", "reservación", "turno", "número de cita"],
    "despedida": ["adiós", "hasta luego", "chao", "bye", "nos vemos"],
    "agradecimiento": ["gracias", "te agradezco", "agradecido", "muchas gracias"]
}

MODEL_DETAILS = {
    "civic": {
        "descripcion": "El Honda Civic es un sedán compacto con motor eficiente y tecnología avanzada.",
        "precio": "El precio base del Honda Civic es $350,000 MXN."
    },
    "cr-v": {
        "descripcion": "El Honda CR-V es un SUV espacioso, ideal para familias y aventuras.",
        "precio": "El precio base del Honda CR-V es $450,000 MXN."
    },
    "accord": {
        "descripcion": "El Honda Accord es un sedán mediano con gran comodidad y potencia.",
        "precio": "El precio base del Honda Accord es $500,000 MXN."
    },
    "fit": {
        "descripcion": "El Honda Fit es un hatchback pequeño y versátil, perfecto para la ciudad.",
        "precio": "El precio base del Honda Fit es $280,000 MXN."
    }
}

def get_intent(text):
    text = text.lower()
    for intent, keywords in INTENT_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                return intent
    return "unknown"

def extract_model(text):
    text = text.lower()
    for model in MODEL_DETAILS.keys():
        if model in text:
            return model
    return None

def process_text(text):
    intent = get_intent(text)

    if intent == "consulta_modelos":
        model = extract_model(text)
        if model:
            detalles = MODEL_DETAILS[model]
            return f"{detalles['descripcion']} {detalles['precio']}"
        else:
            return RESPONSES["consulta_modelos"]

    if intent == "prueba_manejo":
        return RESPONSES["prueba_manejo"]

    return RESPONSES.get(intent, RESPONSES["unknown"])


