import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

def get_candlestick_chart(ticker):
    df = yf.download(ticker, period="3mo", interval="1d")

    
    if df.empty or df.isnull().all().all():
        return go.Figure().add_annotation(
            text="No valid data available for chart.",
            x=0.5, y=0.5,
            showarrow=False,
            font=dict(size=16),
            xref="paper", yref="paper"
        )

    df = df.dropna()
    df = df[df['Open'] > 0]  # remove bad rows
    df.reset_index(inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])

    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        increasing_line_color='green',
        decreasing_line_color='red',
        name='Price'
    ))

    fig.add_trace(go.Bar(
        x=df['Date'],
        y=df['Volume'],
        name='Volume',
        yaxis='y2',
        marker=dict(color='lightblue'),
        opacity=0.4
    ))

    fig.update_layout(
        title=f"{ticker} – 1 Month Candlestick Chart with Volume",
        xaxis=dict(title="Date"),
        yaxis=dict(title="Price", side='left'),
        yaxis2=dict(
            title='Volume',
            overlaying='y',
            side='right',
            showgrid=False
        ),
        height=600,
        margin=dict(l=30, r=30, t=50, b=30),
        legend=dict(orientation='h', y=1.1)
    )

    return fig
