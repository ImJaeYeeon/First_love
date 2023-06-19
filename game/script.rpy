# 게임에서 사용할 캐릭터를 정의합니다.
define m1 = Character('이우주') #남주1 연하 이우주
define m2 = Character('배진혁') #남주2 동갑 배진혁
define m3 = Character('지승현') #남주3 연상 지승현

define rightCharacter = Position(xalign = 0.8, yalign = 0.3)

image background_wish = "달에소원.jpg"
image background_room ="방.jpg"
image background_happyEnding = "happyending.jpg"

image background1_1 = "bg_우주/급식실.jpg"
image background1_2 = "bg_우주/운동장.jpg"
image background1_3 = "bg_우주/교문.jpg"

image background2_1 = "bg_진혁/운동장.jpg"
image background2_2 = "bg_진혁/복도.jpg"
image background2_3 = "bg_진혁/보건실.jpg"

image background3_1 = "bg_승현/도서관.jpg"
image background3_2 = "bg_승현/졸업식.jpg"

image fairy = im.FactorScale("character/요정.png",0.45)


define player_name = "플레이어이름"
define p = Character("player_name",dynamic = True,color="#0B6121")
##Character 일때 player_name은 변수랑 같아야함.

# 여기에서부터 게임이 시작합니다.
label start:

    $player_name = renpy.input("이름을 지정해주세요. 내 이름은")##화면에 내 이름은 나오고 다음칸에 입력받는 칸이 나온다.
    p "내 이름은 [player_name]"##p는 위에 선언한 캐릭터고, 대화창에 변수값을 나오게 할려면 [변수명]으로 사용한다.

    scene background_wish
    p "달님 올해는 꼭 모태솔로 탈출하게 해주세요 .." with fade
    scene background_room
    "아침 7시 알람이 시끄럽게 울린다." with vpunch
    show fairy at rightCharacter
    "..." "네가 [player_name](이)가 맞느냐"  with zoomin
    "..." "나는 어제 네가 불러낸 달의 요정이다.\n너의 소원을 들어주기 위해 네 앞에 나타났다."
    "..." "세 명의 남자 중 마음에 드는 한 명의 남자를 선택해라\n 그 남자가 너의 남자친구가 될 것이다."

    label choice:
    menu :
        "남자를 골라보자"

        "이우주":
            scene background1_3
            "아이돌 연습생 연하남 이우주를 선택했습니다."
            m1 "누나 안녕?ㅎㅎ"
            p "(응? ...누구지? 조금 당황스럽네...)"
            m1 "어...? 누나! 저 기억 안 나요?" with zoomin

            jump start1

        "배진혁":
            scene background2_1
            "같은 반 축구부 배진혁을 선택했습니다."

            jump start2

        "지승현":
            scene background3_1
            "전교1등 선배 지승현을 선택했습니다."

            jump start3

        
#이우주

label start1:
        "뭐라고 대답해야하지..."

        menu:
        
            "글쎄... 잘 모르겠는데?":

                jump ending1

            "아, 당연히 기억하지!":

                jump love1

label love1:

    "두근두근..."

    m1 "누나가 중학교 졸업한 이후로 처음 보네요!"

    "귀엽기만 했던 중학교 후배가 아이돌 연습생이 되어 돌아왔다"

    m1 "아... 벌써 도착했네. 점심 시간에 찾아갈테니까 그 때 봐요 누나!"
    scene background1_1
    "-점심시간(급식실)-"

label cafeteria:
    "우주가 정말 아이돌 연습생이긴 한가보다..."
    "같이 밥을 먹으니 아이들의 이목이 쏠리기 시작한다."

menu:
    "역시 불편한데..."

    "그래도 그냥 참고 먹는다.":

        jump ending2
    
    "부담스러우니 먼저 간다고 말한다.":

        jump love2

label love2:
    "아... 더이상 못 참겠어!"
    p "우주야 미안, 나 먼저 가볼게! 마저 먹고 나와."
    "나는 그대로 자리를 박차고 나왔다."

    m1 "아... 누나! 같이 가요!"

    scene background1_2
    "-운동장-"
label playground:
    m1 "누나... 저 사실...."

    menu:
        "갑자기 진지해졌네... 무슨 일이지?"

        "아... 미안. 나 바쁜 일이 있어서 먼저 갈게 천천히 와.":

            jump ending3

        "응? 무슨 할 말이라도 있어?":

            jump love3
        
    label love3:

        m1 "저.. "

        "???"

        "(심장이 쿵쾅대기 시작한다.)" with vpunch
        
        m1 "중학생 때부터 쭉 누나만을 좋아했어요...! 제가 어떤 모습이어도, 누나는 절 진심으로 사랑해 주실 거 같다는 느낌이 들어요."

        label goback:
        m1 "저랑... 사귀어 주세요...!!"with vpunch

        menu:
            "이건... 너무 갑작스러운데!? 어쩌지..."

            "그래, 나도 사실... 널 좋아했어. 우리 사귀자.":
            
                jump love4

            "저... 우주야 미안... 난 지금이 좋아.":

                jump ending4

label love4:
    scene background_happyEnding
    "이럴수가... 오늘부터 1일!!"
    "이렇게 귀여운 남자친구가 생기다니!"
    "{b}Happy Ending{/b}."

    menu:
        "역시 연하는 내 취향이 아니야! 다른 사람을 만나보겠어!":
            jump choice
        "다른 남자는 필요하지 않아. 이대로 끝낼래요!":
            return

label ending1:

    "내가 대답을 잘 한 게 맞을까?"

    m1 "누나... 너무해요!!"

    "{b}
    다시 잘 생각 해 봐!!\n
    Bad Ending{/b}."  with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump start1
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return

label ending2:
    "참아보려 하지만..."
    "표정관리가 되지 않는다...!"
    
    m1 "저... 누나? 표정이 왜 그래요? 혹시... 저랑 있는 게 부담스러우신 거에요?"

    "의도치 않게 상처를 줘버렸잖아..."
    "{b}Bad Ending{/b}." with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump start1
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return

label ending3:
    "꽤 진지해 보였는데 이야기도 들어주지 않다니 너무하네!"

    "{b}Bad Ending{/b}." with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump start1
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return

label ending4:

    "다 왔는데 이런... 눈치 좀 챙겨 [player_name]!!!"

    "{b}Bad Ending{/b}." with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump start1
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return


# 배진혁

label start2:
    p "아 오늘 체육 있었지..."

    "짝피구...? 내 짝은 누구지?"

    "어, 배진혁...?"

label jin_love1:
    p "아야!"
    "발목을 삐었나..."
    m2 "하, 야 살살 던지라고 했지!" 
    m2 "[player_name], 너 괜찮아? 이리와 보건실 가자."
    m2 "어떻게 보면 내 잘못도 있으니까... 같이 가줄게."

    "어, 같이...?"
    menu:
        "아니야, 괜찮아! 나 혼자 갈 수 있어.":
            jump jin_ending1

        "그래줄래? 고마워." :
            jump jin_love2

label jin_love2:
    scene background2_3
    "진혁이의 부축을 받으며 보건실로 향했지만 보건 선생님은 자리에 계시지 않는다."
    m2 "선생님이 안 계시네."
    "진혁이는 다친 내 발목을 보더니 한숨을 쉰다."
    "내가 뭐라도 잘못했나..."
    label sick:
    m2 "그... 너만 괜찮으면 내가 치료해줄게."
    m2 "네가 알고 있을지 모르겠는데, 나 운동부라서 치료 경험도 꽤 있거든. 안 아프게 해줄게."
    "그걸 모르는 애가 우리학교에 있을 리가..."

    menu:
        "그, 그렇게까지 안 해줘도 돼. 오실 때까지 기다리면 되지!":
        
            jump jin_ending2
        
        "그럼 믿을만 하겠네. 부탁할게.":

            jump jin_love3

label jin_love3:
    scene background2_2
    m2 "자... 다 됐다."
    m2 "[player_name], 혼자 못 걷겠지? 업혀. 교실까지 데려다 줄게."

    "내 나이가 몇인데...!"
    menu:
        "아, 아니야! 충분히 혼자 걸을 수 있어.":
        
            jump jin_ending3
        
        "저, 그럼 잠시 실례할게...":

            jump jin_ending4

label jin_ending1:
    m2 "아... 그래."
    "진혁이는 멋쩍은듯 서있다 돌아가버렸다"
    "부탁했어야지!!"
    "{b}Bad Ending{/b}." with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump start1
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return

label jin_ending2:
    m2 "아... 그래 미안."
    "어색한 공기가 흐른다..."
    "부탁했어야지!!"
    "{b}Bad Ending{/b}." with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump start1
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return

label jin_ending3:
    m2 "그래...? 내가 좀 과했나보네."
    "진혁은 어색하게 웃으며 운동장으로 돌아갔다"
    "부탁했어야지!!"
    "{b}Bad Ending{/b}." with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump start1
        "다른 사람을 만나러 갈래요!":
            jump choice
        "아니요, 그냥 이대로 끝낼게요!":
            return

label jin_ending4:
    "그렇게 진혁이의 등에 업혀 교실까지 올라왔다..."
    "그 전부터 진혁이를 좋아했던 나는 이때를 기회로 용기를 내어본다."

    p "저... 진혁아."
    p "지금 이런 말 하는게 어떻게 들릴지 모르겠지만..."
    p "나, 오래 전부터 널 좋아해왔어."
    p "그러니까 우리... 사귈래?"

    "내 고백을 들은 진혁이는 처음보는 표정을 지으며 고개를 숙였다."
    "쟤도 얼굴이 붉어지긴 하는구나..."

    m2 "응... 좋아."

    scene background_happyEnding
    "{b}Happy Ending{/b}."
    menu:
        "역시 내 취향은 아니야 다른 사람을 만나볼래!":
            jump choice
        "다른 사람은 됐어요! 이대로 끝낼래요!":
            return

# 지승현

label start3:
    "시험기간 도서관에서 침 흘리며 졸고 있는 [player_name]"
    "누군가 다가와 어깨를 톡톡 친다."
    "졸린 눈을 부비며 일어나자..."
    "그... 그 전교 1등 지승현... 선배?"
    "황급히 입가에 묻은 침자국을 지우며 고개를 숙인다."

    p "아, 그... 감사합니다!"

label seng_love1:

    m3 "뭘 감사할 거 까지야. [player_name]... 맞지? 공부 중인 거 같던데, 같이 할래?"
    "내 이름은 어떻게..."
    "아, 이럴 때가 아니지! 뭐라고 대답해야 좋을까..."
    menu:
        "아니에요 선배! 바쁘실 것 같은데 저 혼자 알아서 할게요":

            jump seng_ending1

        "네...! 저도 전교 1등으로 만들어 주세요!" :

            jump seng_love2

label seng_love2:
    
    m3 "그래, 좋아 같이 공부하자 ㅎㅎ"
    m3 "무슨 공부 도와줄까?"

    menu:
        "html이요!":
        
            jump seng_ending2
        
        "미술이요!":

            jump seng_ending3

        "React요!":    

            jump seng_love3

label seng_love3:
    m3 "그래, 리액트 좋네. 옆에 앉아도 되지?"

label graduation:
    scene background3_2
    "승현 선배의 졸업 당일"
    "이제 선배를 학교에서 볼 수 없다니... 눈물이 앞을 가린다."

    menu:
        "이대로 선배를 놓칠 수는 없어! 승현 선배에게 고백한다.":
        
            jump seng_ending4
        
        "다음에 또 만나면 되니까... 내년 ITSHOW에 놀러와 달라고 부탁하며 번호를 남긴다.":

            jump seng_love4

label seng_love4:
    scene background3_3
    "1년 뒤 3학년이 된 미림이의 it쇼 당일"
    "어, 저기... 설마, 승현 선배?!"

    m3 "[player_name]! 고생 많았지? 자 여기 꽃다발."
    "진짜 승현 선배다..."
    menu:
        "1년 만에 만난 승현 선배에게 안기며 고백한다.":
        
            jump seng_ending6
            
        "아, 저... 감사합니다..!!! (부끄러워 한 뒤 도망친다)":

            jump seng_ending5

label seng_ending1:
    m3 "그래.. 나랑 공부하기 싫구나.."
    "선배는 조용히 도서관을 떠난다."
    "같이 했어야지!!"
    "{b}Bad Ending{/b}."
    
    menu:
        "이전으로 돌아갈래요!":
            jump seng_love1
        "남자 선택으로 돌아갈래요!":
            jump choice
        "아니요, 이대로 끝낼래요!":
            return

label seng_ending2:
    m2 "이건 너무 기초인데.. 아직도 모른다니 실망이야"
    m2 "같이 공부하기로 한 건 없던 걸로 하자"
    "기초부터 다지고 다시 도전하자"
    "{b}Bad Ending{/b}." with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump seng_love2
        "남자 선택으로 돌아갈래요!":
            jump choice
        "아니요, 이대로 끝낼래요!":
            return

label seng_ending3:
    m2 "내가 미술은 못 해서.."
    "승현은 당황한 표정을 짓더니 이내 나에게 말을 걸지 않았다."

    "{b}Bad Ending{/b}." with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump seng_love2
        "남자 선택으로 돌아갈래요!":
            jump choice
        "아니요, 이대로 끝낼래요!":
            return

label seng_ending4: 
    m3 "미안 지금은 너무 바빠서.."
    "타이밍을 봐야지!!"
    "{b}Bad Ending{/b}." with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump graduation
        "남자 선택으로 돌아갈래요!":
            jump choice
        "아니요, 이대로 끝낼래요!":
            return

label seng_ending5:
    m3 "아.. 가버렸네..."
    "그렇게 난 다시는 선배를 볼 수 없었다."
    "도망치면 안되지!!"
    "{b}Bad Ending{/b}." with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump seng_love4
        "남자 선택으로 돌아갈래요!":
            jump choice
        "아니요, 이대로 끝낼래요!":
            return

label seng_ending6:
    p "승현 선배.. 아니 승현 오빠! 사실 예전부터 오빠를 좋아했어요!!!"

    m3 "나도 널 좋아했어 우리 사귀자"

    scene background_happyEnding
    "{b}Happy Ending{/b}."
    menu:
        "다른 남자도 만나볼래!":
            jump choice
        "이대로 끝낼래요!":
            return