"""Home page of app"""
import streamlit as st
import pandas_datareader.data as web
import datetime
from database import bdd_setting
from datetime import date, datetime, timedelta
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import pandas as pd


def load_data(tiker, date_start_cotation, date_end_cotation, display_columns=False, columns=False):
    """Able de load data to show in app"""
    data = web.DataReader(tiker, data_source="yahoo", start=date_start_cotation, end=date_end_cotation)
    if display_columns:
        if "," in str(columns):
            data = data[columns]
        else:
            all_col = str(columns)[2:-2]
            data = data[all_col]
    else:
        data = data
    return data


def load_data_for_prediction(ticker, data_start, data_end):
    """specific data for prediction"""
    data = web.DataReader(ticker, data_source="yahoo", start=data_start, end=data_end)
    data.reset_index(inplace=True)
    return data


def app():
    st.session_state.select_columns = False
    st.session_state.add_cours = False
    st.session_state["display"] = False
    data = pd.DataFrame()
    st.title("Plateforme de Trading")
    st.write("Cette application à pour but d'aider à la décision financier dans le cadre"
             "d'investissement boursier")

    if 'ticker' not in st.session_state:
        ticker = st.text_input("Ticker", placeholder="Enter Ticker")
    else:
        ticker = st.text_input("Ticker", placeholder="Enter Ticker", value=st.session_state["ticker"])

    if 'start_date' not in st.session_state:
        date_start_cotation = st.date_input("Date start cotation", date(2012, 12, 21))
    else:
        date_start_cotation = st.date_input("Date start cotation", st.session_state["start_date"])

    if "end_date" not in st.session_state:
        date_end_cotation = st.date_input("Date end cotation")
    else:
        date_end_cotation = st.date_input("Date end cotation", st.session_state["end_date"])

    display_choice = st.radio("Choose your display", ("All data", "Select columns"))

    if display_choice == "Select columns":
        add_cours = st.multiselect("", ("High", "Low", "Close", "Open", "Volume", "Adj Close"))
        st.session_state.add_cours = add_cours
        st.session_state.select_columns = True

    elif display_choice == "All data":
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
            st.subheader('Statistics')
            st.table(data.describe())
            if not st.session_state.select_columns:
                st.subheader('View previous closes')
                st.write(data["Adj Close"].tail(10))
        except:
            st.error("Please, fill all components")

        try:
            if len(st.session_state.add_cours) > 1:
                for column in st.session_state.add_cours:
                    """same_data_to_curve = data
                    x = same_data_to_curve[column]
                    same_data_to_curve.reset_index(level=0, inplace=True)
                    y = same_data_to_curve["Date"]
                    fig, ax = plt.subplots()
                    z = np.polyfit(x, y, 1)
                    y_hat = np.poly1d(z)(x)
                    plt.plot(x, y_hat, "r--", lw=1)
                    ax.scatter(x,y)
                    st.pyplot(fig)"""  # TODO Courbe de tendance
                    # TODO Moyenne mobile des multiples cours

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
        st.subheader('Statistics')
        st.table(st.session_state["data"].describe())
        st.subheader('View previous closes')
        try:
            current_data = st.session_state["data"]
            st.write(current_data["Adj Close"])
        except:
            pass

    if "pseudo" not in st.session_state:
        pass
    else:
        ticker_for_action = ""
        st.title("Trading action")
        result = bdd_setting.see_bdd_of_specific_user(st.session_state["pseudo"])
        actual_capital = result[0][3]
        st.write("Actual Capital : " + str(actual_capital))
        select_order = st.radio("Select multi or simple order", ('Unique', 'Multiple'))

        if select_order == "Multiple":
            number_of_asset = st.slider("How many asset do you want ?", min_value=2, max_value=10)
            if st.button("Put asset"):
                for i in range(number_of_asset):
                    st.text_input("Ticker " + str(i + 1), placeholder="Enter Ticker", key="input" + str(i))
                    # TODO add possibility to do multiple actions
        else:
            ticker_for_action = st.text_input("Ticker", placeholder="Enter Ticker", key="unique_ticker_for_actor")
        action = st.selectbox("Do an action", ("Buy", "Sell"))
        quantity = st.number_input("For how much do you want to put", step=100, min_value=10)
        multiplier_lever = st.number_input("Multiplier Lever", step=1, min_value=1)
        if st.button("Valider mon action"):
            try:
                today = date.today()
                total_transaction = quantity * multiplier_lever
                d = datetime.today() - timedelta(days=1)
                today_for_data = datetime.today().strftime('%Y-%m-%d')

                data = load_data(ticker_for_action, d.strftime('%Y-%m-%d'), today_for_data)
                adj_close = data["Adj Close"].tail(1)
                bdd_setting.put_action_on_db(st.session_state['pseudo'],
                                             today.strftime('%Y-%m-%d %H:%M:%S'),
                                             action, quantity, total_transaction,
                                             multiplier_lever, ticker_for_action, int(adj_close))

                if actual_capital - quantity > 0:
                    bdd_setting.remove_money_from_user_after_validate_action(st.session_state['pseudo'], quantity)
                    st.info("Vous avez validé votre action, elle devrait appraraitre dans la liste des actions")
                else:
                    st.info("Vous n'avez pas assez d'argent sur votre compte pour valider cette action")
            except:
                st.error("Please select a Ticker")

    st.title('Prediction')
    n_month = st.radio('Month of prediction:', [6, 12])
    period = n_month * 31
    if st.button("Do a prediction"):
        prediction(ticker, n_month, period)


def prediction(ticker, n_month, period):
    start = "2017-01-01"
    today = date.today().strftime("%Y-%m-%d")

    data_load_state = st.text('Loading data for prediction since 2017 to today...')
    try:
        data = load_data_for_prediction(ticker, start, today)
        data_load_state.text('Loading data for prediction since 2017 to today... done!')

        st.subheader('Raw data')
        st.write(data.tail())

        plot_raw_data(data)

        # Predict forecast with Prophet.
        df_train = data[['Date', 'Close']]
        # Use Prophet doc
        df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
        m = Prophet()
        m.fit(df_train)
        future = m.make_future_dataframe(periods=period)
        forecast = m.predict(future)

        # Show and plot forecast
        st.subheader('Forecast data')
        st.write(forecast.tail())

        st.write(f'Forecast plot for {n_month} month')
        fig1 = plot_plotly(m, forecast)
        st.plotly_chart(fig1)

        st.write("Forecast components")
        fig2 = m.plot_components(forecast)
        st.write(fig2)

    except:
        st.error("Please select a Ticker")


# Plot raw data
def plot_raw_data(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
