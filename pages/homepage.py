import streamlit as st
import pandas_datareader.data as web
import datetime
from database import bdd_setting
from datetime import date
import random

def load_data(tiker, date_start_cotation, date_end_cotation, display_columns, columns):
    apple_data = web.DataReader(tiker, data_source="yahoo", start=date_start_cotation, end=date_end_cotation)
    if display_columns:
        if "," in str(columns):
            data = apple_data[columns]
        else:
            all_col = str(columns)[2:-2]
            data = apple_data[all_col]
    else:
        data = apple_data
    return data


def app():
    st.session_state.select_columns = False
    st.session_state.add_cours = False
    st.session_state["display"] = False
    st.title("Plateforme de Trading")
    st.write("Cette application à pour but d'aider à la décision financier dans le cadre"
             "d'investissement boursier")

    if 'ticker' not in st.session_state:
        ticker = st.text_input("Ticker", placeholder="Enter Ticker")
    else:
        ticker = st.text_input("Ticker", placeholder="Enter Ticker", value=st.session_state["ticker"])

    if 'start_date' not in st.session_state:
        date_start_cotation = st.date_input("Date start cotation", datetime.date(2012, 12, 21))
    else:
        date_start_cotation = st.date_input("Date start cotation", st.session_state["start_date"])

    if "end_date" not in st.session_state:
        date_end_cotation = st.date_input("Date end cotation")
    else:
        date_end_cotation = st.date_input("Date end cotation", st.session_state["end_date"])

    display_choice = st.radio("Choose your display", ("Unique", "Multiple"))

    if display_choice == "Multiple":
        add_cours = st.multiselect("", ("High", "Low", "Close", "Open", "Volume", "Adj Close"))
        st.session_state.add_cours = add_cours
        st.session_state.select_columns = True

    elif display_choice == "Unique":
        st.session_state.select_columns = False

    if st.button("Display"):
        try:
            data_load_state = st.text('Loading data...')
            data = load_data(ticker, date_start_cotation, date_end_cotation, st.session_state.select_columns,
                             st.session_state.add_cours)
            data_load_state.text("Done!")
            st.write(data)
            st.subheader('Visualisation')
            st.line_chart(data)

        except:
            st.error("Please, fill all components")

        try:
            print(st.session_state.add_cours)
            if len(st.session_state.add_cours) > 1:
                for column in st.session_state.add_cours:
                    print(column)
                    """same_data_to_curve = data
                    x = same_data_to_curve[column]
                    same_data_to_curve.reset_index(level=0, inplace=True)
                    y = same_data_to_curve["Date"]
                    fig, ax = plt.subplots()
                    z = np.polyfit(x, y, 1)
                    y_hat = np.poly1d(z)(x)
                    plt.plot(x, y_hat, "r--", lw=1)
                    ax.scatter(x,y)
                    st.pyplot(fig)"""  # TODO

                    print(column)
                    rendement = (data[column].tail(1).values - data[column].head(1).values) \
                                / data[column].head(1).values
                    st.write("Rendement of " + str(column) + " : " +
                             str(round(rendement[0] * 100)) + "%")
                    if round(rendement[0] * 100) > 1:
                        st.success("Bonne investissement")
                    else:
                        st.error("Mauvais investissement")
            else:
                rendement = (data.tail(1).values - data.head(1).values) / data.head(1).values
                st.write("Rendement : " + str(round(rendement[0] * 100)) + "%")
                if round(rendement[0] * 100) > 1:
                    st.success("Bonne investissement")
                else:
                    st.error("Mauvais investissement")
        except:
            pass

        try:
            st.session_state["ticker"] = ticker
            st.session_state["start_date"] = date_start_cotation
            st.session_state["end_date"] = date_end_cotation
            st.session_state["data"] = data
            st.session_state["display"] = True
        except:
            pass

    if "data" in st.session_state and not st.session_state["display"]:
        st.write(st.session_state["data"])
        st.subheader('Visualisation')
        st.line_chart(st.session_state["data"])

    if 'pseudo' in st.session_state:
        st.write("Do an action")
        action = st.selectbox("Do an action", ("Action 1", "Action 2", "Action 3"))
        quantity = st.number_input("For how much do you want to put", step=100, min_value=10)
        if st.button("Valider mon action"):
            today = date.today()
            if action == "Action 1":
                mutiplicator = 2
            if action == "Action 2":
                mutiplicator = 3
            if action == "Action 3":
                mutiplicator = 4
            else:
                mutiplicator = 1

            indicators = ["indicator1", "indicator2", "indicator3"]
            total_transaction = quantity*mutiplicator
            bdd_setting.put_action_on_db(st.session_state['pseudo'],
                                         today.strftime('%Y-%m-%d %H:%M:%S'),
                                         action, quantity, total_transaction,
                                         random.choice(indicators))
            st.info("Vous avez validé votre action, elle devrait appraraitre dans la liste des actions")


