# brain_lite

stream eeg metrics to terminal

## Emotions

The "met" Stream Labels of EPOC / INSIGHT / FLEX - (with EPOC config only)


| Label | Type | Description |
|:---|:---|:---|
| eng | number | Engagement measures immersion in an activity. |
| exc | number | Excitement measures the intensity of reactions to stimuli or environments. |
| lex | number | Long term excitement. It is calculated from the excitement values of the last minute. |
| str | number | Stress measures emotional tension experienced when completing a task. |
| rel | number | Relaxation measures calm focus after a period of intense concentration. |
| int | number | Interest measures attraction or aversion to stimuli. |
| attention | number | Attention measures sustained focus on a single task. |


Example output

```
t=15.2s eng=0.50, exc=0.27, lex=0.25, str=0.29, rel=0.23, int=0.31, attn=0.58
t=15.8s eng=0.43, exc=0.27, lex=0.25, str=0.34, rel=0.26, int=0.31, attn=0.58
t=16.2s eng=0.34, exc=0.27, lex=0.25, str=0.38, rel=0.30, int=0.32, attn=0.57
t=16.7s eng=0.30, exc=0.27, lex=0.25, str=0.38, rel=0.30, int=0.34, attn=0.57
t=17.2s eng=0.30, exc=0.27, lex=0.25, str=0.38, rel=0.30, int=0.35, attn=0.56
```