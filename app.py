
import streamlit as st
import random

# -----------------------------
# CONFIGURACIÓN DE LA PÁGINA
# -----------------------------

st.set_page_config(
    page_title="Quiz de Machine Learning",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# BANCO DE PREGUNTAS
# -----------------------------

preguntas = [
    {
        "pregunta": "¿Qué es Machine Learning?",
        "opciones": [
            "Una técnica que permite a las computadoras aprender a partir de datos",
            "Un lenguaje de programación",
            "Un tipo de hardware",
            "Un sistema operativo"
        ],
        "respuesta": "Una técnica que permite a las computadoras aprender a partir de datos"
    },
    {
        "pregunta": "¿Cuál de los siguientes es un tipo de Machine Learning?",
        "opciones": [
            "Aprendizaje supervisado",
            "Programación estructurada",
            "Desarrollo web",
            "Computación en la nube"
        ],
        "respuesta": "Aprendizaje supervisado"
    },
    {
        "pregunta": "¿Qué caracteriza al aprendizaje supervisado?",
        "opciones": [
            "El modelo aprende utilizando datos etiquetados",
            "El modelo nunca utiliza datos",
            "El modelo solo trabaja con imágenes",
            "El modelo no necesita entrenamiento"
        ],
        "respuesta": "El modelo aprende utilizando datos etiquetados"
    },
    {
        "pregunta": "¿Cuál es un ejemplo de aprendizaje supervisado?",
        "opciones": [
            "Predecir el precio de una vivienda utilizando datos históricos",
            "Agrupar clientes sin categorías previamente definidas",
            "Reducir la cantidad de variables de un conjunto de datos",
            "Encontrar patrones sin etiquetas"
        ],
        "respuesta": "Predecir el precio de una vivienda utilizando datos históricos"
    },
    {
        "pregunta": "¿Qué caracteriza al aprendizaje no supervisado?",
        "opciones": [
            "Busca patrones o estructuras en datos sin etiquetas",
            "Siempre necesita una variable objetivo",
            "Solo puede utilizar datos numéricos",
            "No utiliza algoritmos"
        ],
        "respuesta": "Busca patrones o estructuras en datos sin etiquetas"
    },
    {
        "pregunta": "¿Cuál es un ejemplo de aprendizaje no supervisado?",
        "opciones": [
            "Agrupar clientes según sus características",
            "Predecir si un correo es spam",
            "Predecir el precio de una casa",
            "Determinar si una imagen contiene un gato"
        ],
        "respuesta": "Agrupar clientes según sus características"
    },
    {
        "pregunta": "¿Qué es un modelo de Machine Learning?",
        "opciones": [
            "Un sistema que aprende patrones a partir de datos para realizar predicciones o decisiones",
            "Un archivo que contiene únicamente imágenes",
            "Un componente físico de una computadora",
            "Una base de datos"
        ],
        "respuesta": "Un sistema que aprende patrones a partir de datos para realizar predicciones o decisiones"
    },
    {
        "pregunta": "¿Para qué se utiliza normalmente un conjunto de datos de entrenamiento?",
        "opciones": [
            "Para que el modelo aprenda patrones",
            "Para apagar el modelo",
            "Para eliminar todos los datos",
            "Para crear una página web"
        ],
        "respuesta": "Para que el modelo aprenda patrones"
    },
    {
        "pregunta": "¿Qué significa hacer una predicción en Machine Learning?",
        "opciones": [
            "Utilizar un modelo entrenado para estimar un resultado",
            "Eliminar los datos de entrenamiento",
            "Cambiar el lenguaje de programación",
            "Crear una nueva computadora"
        ],
        "respuesta": "Utilizar un modelo entrenado para estimar un resultado"
    },
    {
        "pregunta": "¿Cuál de estos puede ser un objetivo de Machine Learning?",
        "opciones": [
            "Clasificar, predecir o encontrar patrones en datos",
            "Reemplazar todos los sistemas operativos",
            "Aumentar físicamente la memoria RAM",
            "Crear electricidad"
        ],
        "respuesta": "Clasificar, predecir o encontrar patrones en datos"
    }
]

# -----------------------------
# GENERAR CUESTIONARIO
# -----------------------------

def generar_quiz():
    preguntas_seleccionadas = random.sample(preguntas, 5)

    quiz = []

    for pregunta in preguntas_seleccionadas:
        opciones = pregunta["opciones"].copy()
        random.shuffle(opciones)

        quiz.append({
            "pregunta": pregunta["pregunta"],
            "opciones": opciones,
            "respuesta": pregunta["respuesta"]
        })

    return quiz


# -----------------------------
# INICIALIZAR EL QUIZ
# -----------------------------

if "quiz" not in st.session_state:
    st.session_state.quiz = generar_quiz()

if "enviado" not in st.session_state:
    st.session_state.enviado = False


# -----------------------------
# TÍTULO
# -----------------------------

st.title("🤖 Quiz de Machine Learning")

st.write(
    "Pon a prueba tus conocimientos básicos sobre "
    "Machine Learning, sus tipos y conceptos generales."
)

st.divider()


# -----------------------------
# FORMULARIO
# -----------------------------

with st.form("quiz_form"):

    respuestas_usuario = []

    for i, pregunta in enumerate(st.session_state.quiz):

        st.subheader(f"Pregunta {i + 1}")

        respuesta = st.radio(
            pregunta["pregunta"],
            pregunta["opciones"],
            key=f"pregunta_{i}"
        )

        respuestas_usuario.append(respuesta)

        st.write("")

    enviar = st.form_submit_button(
        "🚀 Comprobar respuestas",
        use_container_width=True
    )


# -----------------------------
# EVALUAR RESULTADOS
# -----------------------------

if enviar:

    puntaje = 0

    for i, pregunta in enumerate(st.session_state.quiz):

        if respuestas_usuario[i] == pregunta["respuesta"]:
            puntaje += 1

    st.divider()

    # Resultado general
    st.subheader("📊 Resultado")

    st.write(f"Obtuviste **{puntaje} de 5** respuestas correctas.")

    # Animación si todas son correctas
    if puntaje == 5:

        st.balloons()

        st.success(
            "🎉 ¡Excelente! Respondiste correctamente todas las preguntas."
        )

    elif puntaje >= 3:

        st.info(
            "👍 ¡Buen trabajo! Tienes una buena base, "
            "pero todavía puedes seguir practicando."
        )

    else:

        st.warning(
            "📚 Puedes seguir repasando los conceptos básicos "
            "de Machine Learning."
        )

    # -----------------------------
    # MOSTRAR RESPUESTAS
    # -----------------------------

    st.subheader("🔎 Revisión")

    for i, pregunta in enumerate(st.session_state.quiz):

        respuesta_usuario = respuestas_usuario[i]
        respuesta_correcta = pregunta["respuesta"]

        if respuesta_usuario == respuesta_correcta:

            st.success(
                f"**Pregunta {i + 1}: Correcta ✅**"
            )

        else:

            st.error(
                f"**Pregunta {i + 1}: Incorrecta ❌**"
            )

            st.write(
                f"Tu respuesta: **{respuesta_usuario}**"
            )

            st.write(
                f"Respuesta correcta: **{respuesta_correcta}**"
            )

    st.divider()

    # -----------------------------
    # NUEVO QUIZ
    # -----------------------------

    if st.button(
        "🔄 Generar nuevo cuestionario",
        use_container_width=True
    ):

        st.session_state.quiz = generar_quiz()

        st.rerun()
```

### `requirements.txt`



