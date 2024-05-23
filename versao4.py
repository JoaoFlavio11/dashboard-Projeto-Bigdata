import yfinance as yf 
import streamlit as st
import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import plotly.express as px

from pycoingecko import CoinGeckoAPI

# Configuração da página
st.set_page_config(
    page_title="Crypto Tracker",
    page_icon=":coin:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

#HTML header
st.markdown(
    """
    <style>
        header {
            background-color: #0E1117;
            color: #fafafa;
            padding: 15px;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000; /* Garante que o cabeçalho fique sobre o conteúdo */
            display: flex; /* Utiliza o modelo de layout flexível */
            justify-content: space-between; /* Alinha os itens flexíveis no início e no final do contêiner */
            align-items: center; 
        }
        h1 {
            margin: 0; /* Remove a margem padrão do h1 */
        }
        nav ul {
            list-style-type: none;
            padding: 0;
            margin: 0;
            text-align: center;
        }
        nav ul li {
            display: inline-block; /* Exibe os itens na mesma linha */
            margin-right: 10px; /* Adiciona espaço entre os itens */
        }
        nav ul li a {
            color: #fafafa;
            text-decoration: none;
        }

        #MainMenu {
            visibility: hidden;
        }

    </style>

    <header>
        <h1>Crypto Tracker</h1>
        <nav>
            <ul>
                <li><a href="#">Página Inicial</a></li>
                <li><a href="#">Sobre</a></li>
                <li><a href="https://github.com/JoaoFlavio11">Contato</a></li>
            </ul>
        </nav>
    </header>
    """
    ,
    unsafe_allow_html=True
)


# Funções e dados necessários
def get_crypto_price(crypto):
    cg = CoinGeckoAPI()
    price = cg.get_price(ids=crypto, vs_currencies='brl')
    return price[crypto]['brl']

def get_crypto_price2(crypto):
    cg = CoinGeckoAPI()
    price2 = cg.get_price(ids=crypto, vs_currencies='usd')
    return price2[crypto]['usd']

cripto_mapping = {"Bitcoin": "BTC-USD", "Bitcoin Cash":"BCH-USD", "Ethereum": "ETH-USD", "Dogecoin": "DOGE-USD", "Ripple":"XRP-USD", "Litecoin":"LTC-USD", "Solana":"SOL-USD"}


def render_grafico():
    st.markdown("## **Gráfico:** ", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 4])

    with col1:
        cripto_option = st.selectbox("Escolha sua criptomoeda: ", ("Bitcoin", "Bitcoin Cash", "Ethereum", "Dogecoin", "Ripple", "Litecoin", "Solana"))

        start_date = st.date_input("Data Inicial", date.today() - relativedelta(months=1))

        end_date = st.date_input("Data Final", date.today())

        data_interval = st.selectbox("Período:", ("1m", "2m", "5m", "15m", "30m", "1h", "1d", "5d", "1wk", "1mo", "3mo"))

        seletor_de_valor = st.selectbox("Selecionar valor", ("Open", "High", "Low", "Close", "Volume"))
        
        if st.button("Gerar"):
            
            with col2:
                simbolo_cripto = cripto_mapping[cripto_option]
                data_cripto = yf.Ticker(simbolo_cripto)
                cripto_hist = data_cripto.history(start=start_date, end=end_date, interval=data_interval)
                fig = px.line(cripto_hist, x=cripto_hist.index, y=seletor_de_valor, labels={"x": "Date"})
                
                if cripto_option == "Bitcoin":
                    col1, col2 = st.columns([1,2])

                    with col1:
                        st.image(r"C:\Users\JoaoF\OneDrive\Documentos\repositório_teste\economy Tracker\versao4\imgs\bitcoin.png", width=400)
                    with col2:
                        st.write(
                            f"""
                            <span style="font-family: 'Source Sans Pro'; font-weight: bold; font-style: italic; font-size: 30px; color: #f7931a; display: block; text-align: center;">
                                Cotação BRL: R$ {get_crypto_price("bitcoin")} .<br>
                                Cotação USD: US$ {get_crypto_price2("bitcoin")} .
                            </span>
                            """,
                            unsafe_allow_html=True
                        )
                elif cripto_option == "Ethereum":
                    col1, col2 = st.columns([1,2])

                    with col1:
                        st.image(r"C:\Users\JoaoF\OneDrive\Documentos\repositório_teste\economy Tracker\versao4\imgs\ethereum.png", width=400)
                    with col2:
                        st.write(
                            f"""
                            <span style="font-family: 'Source Sans Pro'; font-weight: bold; font-style: italic; font-size: 30px; color: #8c8c8c; display: block; text-align: center;">
                                Cotação BRL: R$ {get_crypto_price("ethereum")} .<br>
                                Cotação USD: US$ {get_crypto_price2("ethereum")} .
                            </span>
                            """,
                            unsafe_allow_html=True
                        )

                elif cripto_option == "Dogecoin":
                    col1, col2 = st.columns([1,2])

                    with col1:
                        st.image(r"C:\Users\JoaoF\OneDrive\Documentos\repositório_teste\economy Tracker\versao4\imgs\dogecoin.png", width=400)
                    with col2:
                        st.write(
                            f"""
                            <span style="font-family: 'Source Sans Pro'; font-weight: bold; font-style: italic; font-size: 30px; color: #f8bf1a; display: block; text-align: center;">
                                Cotação BRL: R$ {get_crypto_price("dogecoin")} .<br>
                                Cotação USD: US$ {get_crypto_price2("dogecoin")} .
                            </span>
                            """,
                            unsafe_allow_html=True
                        )
                st.plotly_chart(fig, use_container_width=True)


# Função para renderizar a seção de cotações
def render_cotacao():
    st.markdown("## **Cotações Atualizadas:** ", unsafe_allow_html=True)

    col1, col2, col3, col4, col5, col6= st.columns(6)

    with col1:
        st.image(r"C:\Users\JoaoF\OneDrive\Documentos\repositório_teste\economy Tracker\versao4\imgs\bitcoin.png", use_column_width=True)

        if st.button("Buscar BTC"):
            st.write(f"""
                    <span style="font-family: 'Source Sans Pro'; font-weight: bold; font-style: italic; font-size: 22px; color: #fafafa; display: block; text-align: center;">
                    Cotação BRL: R$ {get_crypto_price("bitcoin")} .<br>
                    Cotação USD: US$ {get_crypto_price2("bitcoin")} .
                    </span>
                """, unsafe_allow_html=True)
        
        st.write(f"""<hr>""", unsafe_allow_html=True)
        st.image(r"C:\Users\JoaoF\OneDrive\Documentos\repositório_teste\economy Tracker\versao4\imgs\bitcoin.png", use_column_width=True)
        if st.button("Buscar BTH"):
            st.write(f"""
                    <span style="font-family: 'Source Sans Pro'; font-weight: bold; font-style: italic; font-size: 22px; color: #fafafa; display: block; text-align: center;">
                    Cotação BRL: R$ {get_crypto_price("bitcoin-cash")} .<br>
                    Cotação USD: US$ {get_crypto_price2("bitcoin-cash")} .
                    </span>
                """, unsafe_allow_html=True)
            

    with col2:
        st.image(r"C:\Users\JoaoF\OneDrive\Documentos\repositório_teste\economy Tracker\versao4\imgs\ethereum.png", use_column_width=True)

        if st.button("Buscar ETH"):
            st.write(f"""
                    <span style="font-family: 'Source Sans Pro'; font-weight: bold; font-style: italic; font-size: 22px; color: #fafafa; display: block; text-align: center;">
                    Cotação BRL: R$ {get_crypto_price("ethereum")} .<br>
                    Cotação USD: US$ {get_crypto_price2("ethereum")} .
                    </span>
                """, unsafe_allow_html=True)
        
    with col3:
        st.image(r"C:\Users\JoaoF\OneDrive\Documentos\repositório_teste\economy Tracker\versao4\imgs\dogecoin.png", use_column_width=True)

        if st.button("Buscar DOGE"):
            st.write(f"""
                    <span style="font-family: 'Source Sans Pro'; font-weight: bold; font-style: italic; font-size: 22px; color: #fafafa; display: block; text-align: center;">
                    Cotação BRL: R$ {get_crypto_price("dogecoin")} .<br>
                    Cotação USD: US$ {get_crypto_price2("dogecoin")} .
                    </span>
                """, unsafe_allow_html=True)
            
    with col4:
        st.image(r"C:\Users\JoaoF\OneDrive\Documentos\repositório_teste\economy Tracker\versao4\imgs\dogecoin.png", use_column_width=True)

        if st.button("Buscar XRP"):
            st.write(f"""
                    <span style="font-family: 'Source Sans Pro'; font-weight: bold; font-style: italic; font-size: 22px; color: #fafafa; display: block; text-align: center;">
                    Cotação BRL: R$ {get_crypto_price("ripple")} .<br>
                    Cotação USD: US$ {get_crypto_price2("ripple")} .
                    </span>
                """, unsafe_allow_html=True)

    with col5:
        st.image(r"C:\Users\JoaoF\OneDrive\Documentos\repositório_teste\economy Tracker\versao4\imgs\dogecoin.png", use_column_width=True)

        if st.button("Buscar LTC"):
            st.write(f"""
                    <span style="font-family: 'Source Sans Pro'; font-weight: bold; font-style: italic; font-size: 22px; color: #fafafa; display: block; text-align: center;">
                    Cotação BRL: R$ {get_crypto_price("litecoin")} .<br>
                    Cotação USD: US$ {get_crypto_price2("litecoin")} .
                    </span>
                """, unsafe_allow_html=True)

    with col6:
        st.image(r"C:\Users\JoaoF\OneDrive\Documentos\repositório_teste\economy Tracker\versao4\imgs\dogecoin.png", use_column_width=True)

        if st.button("Buscar SOL"):
            st.write(f"""
                    <span style="font-family: 'Source Sans Pro'; font-weight: bold; font-style: italic; font-size: 22px; color: #fafafa; display: block; text-align: center;">
                    Cotação BRL: R$ {get_crypto_price("solana")} .<br>
                    Cotação USD: US$ {get_crypto_price2("solana")} .
                    </span>
                """, unsafe_allow_html=True)

                
# Função para renderizar a seção "Sobre nós"
def render_sobre_nos():

    st.markdown(""" 
        ## Sobre nós:

        O **Crypto Tracker** é uma ferramenta poderosa projetada para acompanhar a cotação atual e gerar gráficos detalhados das principais criptomoedas, incluindo Bitcoin, Ethereum e Dogecoin. Com interface intuitiva e funcionalidades abrangentes, este aplicativo oferece uma visão completa do mercado de criptomoedas em tempo real.

        **Recursos Principais:**

        - **Cotação em Tempo Real:** Acompanhe o preço atual das criptomoedas em relação ao BRL (Real Brasileiro).

        - **Análise de Dados:** Gere gráficos dinâmicos e informativos para visualizar tendências de preço ao longo do tempo.

        - **Seleção Personalizada:** Escolha sua criptomoeda de interesse e ajuste o período de análise conforme suas necessidades.
        <hr>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(" ### Doações em BTC: ")
        st.image(r"C:\Users\JoaoF\OneDrive\Documentos\repositório_teste\economy Tracker\versao4\imgs\qrcode_wallet.jpeg", use_column_width=True)

    with col2:
        st.markdown(" ### Doações: ")
        st.image(r"C:\Users\JoaoF\OneDrive\Documentos\repositório_teste\economy Tracker\versao4\imgs\bin_any_final.jpeg", use_column_width=True)
        
    with col3:
        st.markdown(" ### Doações em BTC: ")
        

    with col4:
        st.markdown(" ### Doações em BTC: ")
        

# Selecionando a seção a ser exibida
menu_options = ["Gráfico", "Cotações", "Sobre nós"]
selection = st.sidebar.radio("Selecione uma opção:", menu_options)


# Renderizando a seção selecionada
if selection == "Gráfico":
    render_grafico()
elif selection == "Cotações":
    render_cotacao()
elif selection == "Sobre nós":
    render_sobre_nos()

# HTML footer
st.markdown(
    """
    <style>
        
        footer {
            background-color: #16161a;
            color: #fafafa;
            padding: 9px;
            text-align: center;
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        footer p {
        margin: 0; 
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>

    <footer>
        <p> Desenvolvido por João Flávio C. Lopes | &copy; 2024 Crypto Tracker. Todos os direitos reservados. </p>
    </footer>
    """
    ,
    unsafe_allow_html=True
    
)

#link das imagens 
#<a href="https://iconscout.com/icons/bitcoin" class="text-underline font-size-sm" target="_blank">Bitcoin</a> by <a href="https://iconscout.com/contributors/symbolon-studio" class="text-underline font-size-sm" target="_blank">Symbolon Studio</a>

#<a href="https://iconscout.com/icons/dogecoin" class="text-underline font-size-sm" target="_blank">Dogecoin</a> by <a href="https://iconscout.com/contributors/vladislav-sergeev-1" class="text-underline font-size-sm">Vladislav Sergeev</a> on <a href="https://iconscout.com" class="text-underline font-size-sm">IconScout</a>

#<a href="https://iconscout.com/icons/ethereum" class="text-underline font-size-sm" target="_blank">Ethereum</a> by <a href="https://iconscout.com/contributors/icon-54" class="text-underline font-size-sm" target="_blank">Icon 54</a>