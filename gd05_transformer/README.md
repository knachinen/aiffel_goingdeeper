# AIFFEL Campus Online 5th Code Peer Review Templete
- 코더 : 김성진
- 리뷰어 : 김연수


# PRT(PeerReviewTemplate) 
각 항목을 스스로 확인하고 토의하여 작성한 코드에 적용합니다.

- [X] 코드가 정상적으로 동작하고 주어진 문제를 해결했나요?
    
    네, 정상적으로 동작하며 주어진 과제를 해결합니다.
- [X] 주석을 보고 작성자의 코드가 이해되었나요?

    네, 주석과 마크다운을 많이 달아주셔서 전반적인 코드 이해에 도움이 되었습니다.
- [X] 코드가 에러를 유발할 가능성이 없나요?
  
    에러 없이 모두 잘 작동하는 것으로 보입니다.
- [X] 코드 작성자가 코드를 제대로 이해하고 작성했나요?
  
    네, 주석과 마크다운 내용으로 보아 코드에 대한 전반적인 이해를 바탕으로 작성하신 것 같습니다.
- [X] 코드가 간결한가요?
  
    네, 간결합니다.

# 예시
1. 주석을 보고 작성자의 코드가 이해되었습니다.
```python
 def generate_tokenizer(self, corpus, vocab_size, file_name_prefix="00", model_type="unigram"):

        self.prefix = f'{file_name_prefix}_spm'   # 저장될 tokenizer 모델에 붙는 이름
        self.vocab_size = vocab_size  # vocab 사이즈
        self.model_type = model_type  # Choose from unigram (default), bpe, char, or word
        self.inputs = f'{file_name_prefix}_temp.txt'  # temporary file name
        
        self._write_to_temp(corpus)
        self._train_spm()
        
        # Load the trained model
        tokenizer = spm.SentencePieceProcessor()
        if not tokenizer.Load(f'{self.prefix}.model'):
            logging.error("Failed to load the trained SentencePiece model.")
            return None

        # Clean up temporary files
        os.remove(self.inputs)
        logging.info(f"Temporary file {self.inputs} removed.")

        return tokenizer
```

2. BPE 방식을 적용해 보시고 그 결과를 그래프로 비교해주신 점이 좋았습니다.

3. 학습하신 내용과 결과에 대해 리뷰가 잘 작성되어 있었습니다.
    ```markdown
    핵심 키워드가 포함되기는 해서, 적어도 앞서서 구현한 seq2seq 모델보다는 나은 결과를 보여준다.
    오바마 - obama, 도시 - city, 필요 - need, 일곱 - seven, 사망자 - killed
    학습이 진행되면서 결과가 좀 더 안 좋아지기도 한다.
    과대적합때문일 수도 있겠지만, 더 나은 결과를 보여주는 문장도 있어서 꼭 그렇다라고도 보기는 애매하다.
    ```


