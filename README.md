## Antichrist Blog
Telegram - [Antichrist (Creator)](https://t.me/antichristone), subscription or life?


## Python3 [demo](https://t.me/antichristone/273) (algorithm)

```
from neuron import AI
ai=AI()

face=ai.face_id('model_1.jpg') 
face2=ai.face_id('model_2.jpg') 

print(ai.face_comparison(face, face2))
0.6043529103347101

for photo in ['1.jpg', '2.jpg', '3.jpg', '4.jpg']:
    result=ai.face_comparison(face, ai.face_id( photo ) )
    if result < 5.0:
       print(f"Similarity: {photo} | {result}")
       #ai.creating_a_photo(photo)
```








