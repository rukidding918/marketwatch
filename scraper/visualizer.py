import plotly.graph_objects as go
from plotly.subplots import make_subplots


def visualize(data=None, benchmark='종가', overlaps=['PBR']):
    if not data:
        from scraper.scraper import get_index_data
        data = {'KOSPI': get_index_data()}

    rows = len(data)
    cols = len(overlaps)

    specs = [[{"secondary_y": True}] * cols] * rows
    subplot_titles = []
    for key in data:
        for overlap in overlaps:
            last_day = data[key].index[-1].strftime('%Y-%m-%d')
            ratio = str(data[key][overlap][-1])
            subplot_titles.append(f'{key} {benchmark}와 {overlap}<br>{last_day}: {ratio}')
    # subplot_titles = [f'{key} {benchmark}와 {overlap}' for key in data for overlap in overlaps]

    fig = make_subplots(rows=rows, cols=cols, 
                        specs=specs,
                        subplot_titles=tuple(subplot_titles),
                        # shared_xaxes=True,
                        vertical_spacing=0.35,
                        )
    for row, (key, df) in enumerate(data.items(), start=1):
        for col, overlap in enumerate(overlaps, start=1):
            mean = df[overlap].mean()
            fig.add_trace(
                go.Scatter(x=list(df.index), y=list(df[overlap]), name=overlap),
                secondary_y=False,
                row=row, col=col
            )
            fig.update_yaxes(title_text=overlap, secondary_y=False)

            fig.add_trace(
                go.Scatter(x=list(df.index), y=list(df[benchmark]), name=key),
                secondary_y=True,
                row=row, col=col
            )
            fig.update_yaxes(title_text=benchmark, secondary_y=True)

            fig.add_shape(type='line', x0=df.index[0], y0=mean, x1=df.index[-1], y1=mean, row=row, col=col)

    fig.write_html('index.html')

    return 
