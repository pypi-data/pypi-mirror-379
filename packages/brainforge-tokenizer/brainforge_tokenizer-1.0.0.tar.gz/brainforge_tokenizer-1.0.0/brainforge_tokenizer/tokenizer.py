import tiktoken
import json
import urllib.request

# 🔥 VOCAB DATA EMBEDDED (or download from URL)
VOCAB_URL = "https://your-server.com/vocab.json"  # Your vocab file online

def get_brainforge():
    """Get BrainForge tokenizer from anywhere!"""
    
    try:
        # Download vocab from URL
        with urllib.request.urlopen(VOCAB_URL) as response:
            vocab = json.loads(response.read().decode())
        
        # Create byte vocab
        byte_vocab = {}
        for i in range(256):
            byte_vocab[bytes([i])] = i
        
        for token, token_id in vocab.items():
            try:
                byte_vocab[token.encode('utf-8')] = token_id
            except:
                continue
        
        # Create tiktoken encoding
        return tiktoken.Encoding(
            name="brainforge_tokenizer",
            pat_str=r"""[a-zA-Z_]\w*|\d+|[^\r\n\p{L}\p{N}]?\p{L}+|\p{N}{1,3}| ?[^\s\p{L}\p{N}]+[\r\n]*|\s*[\r\n]+|\s+(?!\S)|\s+""",
            mergeable_ranks=byte_vocab,
            special_tokens={}
        )
        
    except Exception as e:
        print(f"❌ Error loading BrainForge tokenizer: {e}")
        return None
