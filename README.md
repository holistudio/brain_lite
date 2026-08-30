# brain_lite

stream eeg metrics from Emotiv Insight to terminal

## Emotions

The "met" Stream Labels of Emotiv Insight headset


| Psychology Term | Label | Type | Description |
|:---|:---|:---|:---|
| Boredom (inverse) | eng | number | Engagement measures immersion in an activity. |
| Arousal | exc | number | Excitement measures the intensity of reactions to stimuli or environments. |
| Arousal (sustained) | lex | number | Long term excitement. It is calculated from the excitement values of the last minute. |
| Frustration | str | number | Stress measures emotional tension experienced when completing a task. |
| Meditation | rel | number | Relaxation measures calm focus after a period of intense concentration. |
| Valence | int | number | Interest measures attraction or aversion to stimuli. |
| Focus | attention | number | Attention measures sustained focus on a single task. |

## Usage

After setting up virtual environment, install requirements

```
(uv) pip install -r requirements.txt
```

Run

```
python stream.py
```

Example output

```
t=15.2s eng=0.50, exc=0.27, lex=0.25, str=0.29, rel=0.23, int=0.31, attn=0.58
t=15.8s eng=0.43, exc=0.27, lex=0.25, str=0.34, rel=0.26, int=0.31, attn=0.58
t=16.2s eng=0.34, exc=0.27, lex=0.25, str=0.38, rel=0.30, int=0.32, attn=0.57
t=16.7s eng=0.30, exc=0.27, lex=0.25, str=0.38, rel=0.30, int=0.34, attn=0.57
t=17.2s eng=0.30, exc=0.27, lex=0.25, str=0.38, rel=0.30, int=0.35, attn=0.56
```