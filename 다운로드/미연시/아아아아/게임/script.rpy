# 게임에서 사용할 캐릭터를 정의합니다.
image bg="도서"
image bg1="으슥"
image bg2="제목 없음"
define game = Character('개발자',kind=nvl)
define na = Character(None,kind=nvl)
image don = "돈"
image dum="운동"
image book = "책"
image ga="가면"

# 여기에서부터 게임이 시작합니다.
label nothing:
   game "개발자가 힘들어서 남캐는 없대 너무 슬프다 ㅡㅎㄱ흑"
   nvl clear
label start:
game  "시간이 없어서 배경 잘리고"
game "캐릭터도 없고 "
game "선택지도 거의 없고"
game "퀄리티가 조악하대"
game "너무 슬프다 흑흑"
nvl clear
menu oo:
    "뭐가 좋으세요?"
    "여자":
      jump n
    "남자":
      jump nothing

label n:  
    scene bg2     
    "나" "학교 가야하는 데 가기싫다..."
    "나" "가지말까..."
    "쾅!" with vpunch
    show dum
    "김소꿉" "야 일어난거 다 아니깐 일어나라 오늘 입학식인거 모르냐?!"
    "나" "(저녀석은 내 소꿉친구인 김소꿉이다 나같은것을 위해 직접깨워주는 친절한녀석)"
    "나" "예~예~"
    "나" "'우리는 같이 등교하며 담소를 나누며 학교로 향했다'"
    "빵! 끼이익!!" with vpunch
    "?" "하.. 아침부터 재수없게"
    "내가 치일뻔한 차에 창문을 내리며 우리학교 교복을 입은 여자가 말했다"
    "김소꿉" "야 사람이 치일뻔했는데 무슨 말이 그러냐??"
    "?" "그러게 잘 보고 다녔어야지"
    "그 말을 후에 자동차는 사라졌다"
    "김소꿉" "네가 다칠뻔 했는데 사과도 없이...!"
    "나" "됐어 안 죽었으면 됐지"
    "나" "난 네가 나 대신 화내주는것만으로도 충분해  "
    "김소꿉" "넌 진짜...아니됐다..."
    "우리는 그렇게 학교강당에 도착했다"
    "-강당에서의 입학식과 교장의 연설이 끝난후-"
    "김소꿉" "야 동아리 같이 하자"
    "나" "무슨동아리?"
    "김소꿉" "기초체력증진 동아리"
    "김소꿉" "너 아침마다 못 일어나는거 보면 체력부족때문이니깐 같이하면 딱이잖아"
    "김소꿉" "내가 도와줄께"
    "나" "으음...생각해 볼께"
    "김소꿉" "그럼 난 부실로 간다"

    menu 선택:
        "(일단 둘러보자)"
        "도서관":
            "나" "(차분한곳이 좋겠어)"
            "나" "난 도서관 좀 둘러 볼께"
            jump next1
        "소꿉친구의 동아리":
            "나" "(아는 사람이 있는게 좋겠지)"
            "나" "야 같이 가자"
            jump next2
        "으슥한 곳":
            "나" "(즐거움을 위해선 위험을 감수해야지)"
            jump next3

    return

label next1:
    scene bg
    "나" "오오 여기가 도서관"
    "쓰읍 하~"
    "푸흡"
    "난 웃음소리가 난 곳으로 눈을 돌렸다"
    show book
    "?" "아 미안! 웃을 생각은 아니었는데..."
    "그곳에는 작지만 맑은 목소리를 가진 여성이 책을 들고 서있었다"
    "?" "미안해 나랑 비슷한 반응이라...무심결에..."
    menu 선택2:
        "(어떻게 하지))"
        "누군지 물어보자":
            "나" "저..근데 누구세요?"            
            jump next11
        "소꿉친구의 동아리로 도망치자":
            "나" "(역시 아는 사람이 편하겠어)"
            "나" "안녕히 계세요"
            jump next2
        "으슥한 곳으로 도망치자":
            "나" "(쪽팔리니깐 도망쳐야지)"
            jump next3

label happy:
    scene black with dissolve
    "나는 연애 끝에 결혼을 했대 너무 기쁘다 ㅎㅎ"
return
label bad:
    scene black with dissolve
    "나는 아무것도 못 하는 모쏠이래 너무 슬프다 흑흑 "
return
label next11:
    scene bg
    show book
    "도서부" "아 난 도서부의 2학년 '도서부'라고해 아까 웃어서 미안해"
    "나" "이제 그만 사과하셔도 돼요."
    "나" "으음...서부..선배..님?"
    "도서부" "고마워 그리고 그냥 선배라고 불러도 돼"
    "나" "아 넵 근데 아까 선배랑 비슷한 반응이라고 하신건?"
    "도서부" "내가 책냄새를 좋아해서 나도 그랬었거든"
    "도서부" "너도 좋아하니? 책냄새"
    "나" "네 좋아하는 편이에요 맡는것 만으로도 머리가 좋아지는 느낌이라서"
    "도서부" "푸훗 재미있는 표현이네"
    "나" "그런가요 도서부라고 하셨는데 도서부에서 뭐해요?"
    "도서부" "책 정리도 하고,"
    "나" "음음"
    "도서부" "독서토론도 해"
    "나" "어..음.."
    "도서부" "혜택도 있어 먼저 신권을 읽을 수 있고.."
    "나" "..."
    "도서부" "사서 선생님이 먹을것을 사주시기도 해"
    "나" "입부신청서는 어디에내죠?"
    "도서부" "푸훗 먹을것 때문에 입부하는 거야?ㅋㅋ"
    "나" "꼭 그런것만은 아니죠..."
    "이 대화가 엇그제같은데...벌써 1년이 지났다니"
    "서부선배도 나한테 관심있어 보이던데 고백해도 도ㅣ지 않을까?"
    menu 선택tt:
        "(나는 선배한테 말를...)"
        "걸어서 데아트 산청을 한다":
            "나" "서부선배, 선배가 좋아한했던 감독의 영화 개봉했는데 보셨어요?" 
            "도서부" "아니 아직 못 봤어"
            "나" "그럼 같이 보러 가실래요?"
            "도서부" "그래 좋아!"           
            jump next111
        "걸지 않는다":
            "나" "아니 역시 이건 좀 아닌것 같아"
            jump bad
label next111:
    "우리는 하늘이 까메져서야 집으로 향했다"
    "도서부,나" "저기"
    "우리는 동시에 말을 걸었다"
    menu 선택2222:
        "도서부" " 너 먼저 해" 
        "먼저 말 한다":
            "나는 나의 마음을 전했다" 
            "도서부" "나도 좋아해"      
            jump happy
        "먼저 말 하지 않는다":
            "나" "먼저 말씀해주세요"
            "도서부" "처음 봤을때 재밌는 친구라 생각했고 친절하게 대해준 네가 좋아"
            "나" "저도 그래욘"
            jump happy
return

label next2:
    scene bg2
    show dum
    "김소꿉" "뭐야 같이하자고 할때는 떨떠름한 표정이더니"
    "나" "생각해보니 내가 중학교때 이사갔다와서 아는 사람이없어"
    "김소꿉" "ㅋㅋ넌 나 없으면 어떡하냐"
    "나" "그러게 어떡하지 등굣길에서도 네가 끌러줘서 차에 안 치이고" 
    "나" "나 너 없이 어떻게 살지?"
    "김소꿉" "(화-악)"
    "김소꿉" "///뭐래///진짜///"
    "김소꿉" "크흠, 아무튼 앞으로 이 누님 옆에 딱붙어 다녀라"
    "김소꿉" "알겠냐?"
    "나" "넵! 누님!"
    "김소꿉" "그럼이제 가자"
    "우리는 부실로 향햤고 입부신청서를 낸 뒤 교실로 돌아왔다"
    "김소꿉" "야 동아리 재미있을것 같지 않냐?"
    "나" "내가 저질체력으로 고통 받는 모습이?"
    "김소꿉" "아니 네가 점점 건강해질 모습이"
    "나" "그게 그거 아닌가"
    "김소꿉" "틀리거든!"
    "김소꿉" "그리고..."
    "나" "그리고?"
    "김소꿉" "///아니다...///"
    "나" "왜 말을 하다 말아"
    "김소꿉" "됐어"
    "나" "야 근데 나 안 허약하거든"
    "김소꿉" "뭐래 완전 허약한데"
    "나" "아니거든"
    "김소꿉" "응 아니야~"
    menu 선택21:
        "김소꿉" "주말에 운동하러 우리집으로 와라"
        "알겠어":
            "김소꿉" "그래 잘들어가"  
            "그후 난 주말에 소꿉이의 집으로 향했다" 
            jump next22
        "...":
            "김소꿉" "와라 안 오면 내가 찾아감"
            "주말이 도ㅐ자 나는 소꿉이가 못들어오게 비밀번호를 바꾸고 차단을 했다"
            jump bad
label next22:
    scene bg2
    show dum
    "김소꿉" "이런 대화한게 벌써 반년 전이네... "
    "나" "뭐가?"
    "김소꿉" "니 멋있어졌다고"
    "나" "니가 주말에도 운동시켰으나깐..."
    "김소꿉" "야"
    "나" "음?"
    "김소꿉" "나랑 사귀자"
    "나" "푸흡, 켈록 켈럭 쓰으읍 뭔"
    menu 손탹:
        "김소꿉" "진심이야"
        "좋아":
            jump happy
        "미안":
            "김소꿉" "...그러냐"
            jump bad
label next3:
    scene bg1
    "학폭현장을 발견해 버렸다"
    show don
    "근데 괴롭힘 당하는 놈이 날 차로 칠 뻔한 놈이네"
    "일찐" "이름이...이..사장?"
    "이사장" "뭐"
    "일찐2" "엌ㅋㅋㅋ어떻게 사람이름이 잌ㅋㅋ사ㅋㅋㅋ장ㅋㅋㅋㅋ" 
    menu 선택3333:
        "이름이 이사장이었군"
        "이름을 가지고 놀리다니...이렇게 가면..."
        "라이더!":
            show ga
            na "'크아아아아'
            가면중에서도 최강의 가면라이더가 울부짓었다
            가면라이더는 졸라짱쎄서 라이더중에서 최강이엇다
         일찐이나 일찐2도 이겼따 다덤벼도 이겼따 가면라이더는
            새상에서 하나였다 어쨌든 걔가 울부짓었따
            '으악 제기랄 도망가자'
            이사장이 도망갔다 가면라이더가 짱이었따
            그래서 이사장은 도망간 것이다"
            nvl clear  
            jump gamun
        "도망치자":
            
            jump bad
label gamun:
    "이사장녀석 도와줬는데 도망가다니"
    menu tjtjd:
        "어떻게 할까"
        "이사장을 잡는다":
            na "가면라이더는 가면라이더로 변했는데 대단한 꽃미남이라 
            여자 남자는 물론 이사장조차도 
            반하게 만들었다 그러나 역시 가면이기 때문에 보이지 않느다"
            nvl clear
        "이사장을 놔둔다":
            jump bad
        
