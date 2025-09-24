# Update brainforge_tokenizer/tokenizer.py
import tiktoken
import json
import pkg_resources

def get_brainforge():
    """Get BrainForge tokenizer with embedded vocab"""
    try:
        # Load vocab from package data
        vocab_data = pkg_resources.resource_string('brainforge_tokenizer', 'vocab.json')
        vocab = json.loads(vocab_data.decode('utf-8'))
        
        byte_vocab = {}
        for i in range(256):
            byte_vocab[bytes([i])] = i
        
        for token, token_id in vocab.items():
            try:
                byte_vocab[token.encode('utf-8')] = token_id
            except:
                continue
        
        return tiktoken.Encoding(
            name="brainforge_tokenizer",
            pat_str=r"""[a-zA-Z_]\w*|\d+|[^\r\n\p{L}\p{N}]?\p{L}+|\p{N}{1,3}| ?[^\s\p{L}\p{N}]+[\r\n]*|\s*[\r\n]+|\s+(?!\S)|\s+""",
            mergeable_ranks=byte_vocab,
            special_tokens={}
        )
        
    except Exception as e:
        print(f"❌ Error loading BrainForge tokenizer: {e}")
        return None
