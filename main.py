import streamlit as st
import streamlit.components.v1 as components

# Configuración básica de la página para dispositivos móviles
st.set_page_config(
    page_title="¿Alitas Acevichadas?",
    page_icon="🍗",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilos CSS para pantalla completa, colores y botones grandes
st.markdown("""
    <style>
    /* Ocultar elementos predeterminados de la interfaz de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background-color: #FFF5F5;
    }
    
    .main-title {
        font-size: 36px !important;
        font-weight: 900;
        color: #D90429;
        text-align: center;
        margin-top: 15vh;
        margin-bottom: 40px;
        line-height: 1.3;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding: 0 10px;
    }
    
    /* Estilo del botón principal */
    .stButton>button {
        display: block;
        margin: 0 auto;
        background: linear-gradient(135deg, #EF233C, #D90429);
        color: white;
        font-size: 24px;
        font-weight: bold;
        padding: 18px 40px;
        border-radius: 50px;
        border: none;
        box-shadow: 0px 10px 20px rgba(217, 4, 41, 0.4);
        transition: all 0.3s ease 0s;
        cursor: pointer;
    }
    
    .stButton>button:active {
        transform: scale(0.95);
    }
    </style>
""", unsafe_allow_html=True)

# Pregunta en texto grande
st.markdown('<div class="main-title">¿Quieres comer unas alitas acevichadas conmigo? 🍗✨</div>', unsafe_allow_html=True)

# Botón interactivo
if st.button("¡Sí, me encantaría! ❤️"):
    # Animación de explosión masiva de corazones rojos en movimiento
    components.html("""
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
        <script>
            // Definición de la forma del corazón
            var heart = confetti.shapeFromPath({
                path: 'M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z'
            });

            var duration = 3.5 * 1000;
            var animationEnd = Date.now() + duration;

            // Ráfaga inicial en el centro
            confetti({
                particleCount: 60,
                spread: 100,
                origin: { y: 0.6 },
                shapes: [heart],
                colors: ['#FF0000', '#D90429', '#EF233C', '#FF4D6D', '#800020'],
                scalar: 2.2
            });

            // Lluvia/Explosión continua desde varios ángulos
            (function frame() {
                var timeLeft = animationEnd - Date.now();

                confetti({
                    particleCount: 12,
                    startVelocity: 35,
                    spread: 360,
                    ticks: 120,
                    origin: { x: Math.random(), y: Math.random() - 0.2 },
                    shapes: [heart],
                    colors: ['#FF0000', '#D90429', '#EF233C', '#FF70A6'],
                    scalar: Math.random() * (2.5 - 1.2) + 1.2
                });

                if (timeLeft > 0) {
                    requestAnimationFrame(frame);
                }
            })();
        </script>
    """, height=0)
    
    st.balloons()
    st.success("¡Genial! ¡Queda pactado para ir por esas alitas! 😋")