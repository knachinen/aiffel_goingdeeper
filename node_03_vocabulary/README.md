# AIFFEL Campus Online 5th Code Peer Review Templete
- 코더 : 김성진
- 리뷰어 : 손정민


# PRT(PeerReviewTemplate) 
각 항목을 스스로 확인하고 토의하여 작성한 코드에 적용합니다.

- [x] 코드가 정상적으로 동작하고 주어진 문제를 해결했나요?
  
- [ ] 주석을 보고 작성자의 코드가 이해되었나요?
- [x] 코드가 에러를 유발할 가능성이 없나요?
    RAM 용량 초과로 로딩이 되지 않은 부분이 있었지만 과제에 필수적인 부분은 아니었고, 나머지 부분은 잘 실행되었습니다.
- [x] 코드 작성자가 코드를 제대로 이해하고 작성했나요?
    다양한 실험을 한 것으로 보아 제대로 이해하고 여러 조건 하에서 시도한 것으로 보입니다. mecab, komoran, word2vec, fasttext 등의 방법을 추가적으로 사용하였습니다.
- [x] 코드가 간결한가요?
    직관적인 변수명을 사용하였고, 적절한 개행을 사용하여 코드를 간결하게 구성했습니다.
    ```python
    ...
    embedding_dim = ftk.vector_size
    model_name = "ftk_emb128_patience5"
    model_desc = "Mecab, FastText, embedding 128, LSTM 128, Patience 5"
    vocab_size = len(tokenizer_mecab.word_index) + 1
    ...
    ```
# 참고 링크 및 코드 개선
제 수준에서 개선할 부분은 보이지 않지만, 주석이 더 상세하게 있었다면 좋았을 것 같습니다. 다양한 조건에서의 모델을 구성한 것, 깔끔한 시각화가 돋보였고 시각화 단계에서의 모델 간 비교나 과적합 여부에 대한 분석이 인상적이었습니다.
> SentencePiece VS. KoNLPy 등 다른 모델들과 비교
> - SentencePiece 기본값인 unigram 보다 bpe 가 조금 나은 결과를 보여주었다.
> - KoNLPy Mecab 형태소 분석기를 쓴 모델이 SentencePiece 모델 보다 조금 더 나은 결과가 나왔다.
> - Mecab 을 쓴 데이터로 Word2Vector 를 거친 모델이 제일 좋은 결과를 보여주었다.
> - LSTM 128에서 64로 줄여보니 결과는 더 안좋아진다.

> 과적합 
> - 전체적으로 과적합 양상이 보인다.
> - Dropout 레이어를 0.1, 0.2 값으로 추가해봤는데, 전혀 학습이 되지 않았다.
> - L2, BatchNormalization, Dropout 추가: 학습은 되는데, 성능이 좋지 않다.
> - L2, BatchNormalization, Dropout 넣고 빼고 해본 결과 다 빼는 것이 제일 낫다.
> - SentencePiece 결과중에서는 단순하게 LSTM 128 레이어 하나만 가진 모델이 제일 좋은 결과를 보여주었다.
