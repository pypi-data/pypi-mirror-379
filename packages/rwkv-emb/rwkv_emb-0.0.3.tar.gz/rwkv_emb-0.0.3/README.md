The RWKV-X Language Model

https://github.com/howard-hou/EmbeddingRWKV

```python
# !!! set these before import RWKV !!!
import os

os.environ["RWKV_CUDA_ON"] = '0' # '1' to compile CUDA kernel (10x faster), requires c++ compiler & cuda libraries

from rwkv_emb.model import EmbeddingRWKV

EOS_INDEX = 65535
# download models: to be announced
model = EmbeddingRWKV(model_path='path-to-model', strategy='cpu fp32')


# !!! model.forward(tokens, state) will modify state in-place !!!

emb, state = model.forward([187, 510, 1563, 310, 247, EOS_INDEX], None)
print(emb.detach().cpu().numpy())                   # get logits
emb, state = model.forward([187, 510], None)
emb, state = model.forward([1563], state)           # RNN has state (use deepcopy to clone states)
emb, state = model.forward([310, 247, EOS_INDEX], state)
print(emb.detach().cpu().numpy())                   # same result as above
print('\n')
```