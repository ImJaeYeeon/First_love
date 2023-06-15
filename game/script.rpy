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
            p "누구지? 당황스럽다.."
            m1 "누나! 저 기억 안 나요?" with zoomin

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
        "헉.. 뭐라 대답해야 할까?"

        menu:
        
            "어.. 잘 모르겠는데?":

                jump ending1

            "당연히 기억하지!":

                jump love1

label love1:

    "두근두근.."

    m1 "누나가 중학교 졸업한 이후로 처음 보네요!"

    "귀엽기만 했던 중학교 후배가 아이돌 연습생이 되어 돌아왔다"

    m1 "아.. 벌써 학교네요. 이따 점심 시간에 봐요 누나!"
    scene background1_1
    "-점심시간(급식실)-"

label cafeteria:
    "급식실에서 우주랑 밥을 먹으니 이목이 쏠린다..."

menu:
    "이 때 나의 선택은?"

    "그래도 그냥 참고 먹는다.":

        jump ending2
    
    "부담스러우니 먼저 간다고 말한다.":

        jump love2

label love2:
    "자리를 박차고 나온 [player_name]"

    m1 "아, 누나 같이 가요!"

    scene background1_2
    "-운동장-"
label playground:
    m1 "누나... 저 사실...."

    menu:
        "무슨 이야기를 하려고 그러지?"

        "응? 뭐라고? 나 바쁜 일이 있어서 먼저 갈게 천천히 와":

            jump ending3

        "응? 무슨 일인데?":

            jump love3
        
    label love3:

        m1 "저.. "

        "???"

        "(심장이 쿵쾅대기 시작했다)" with vpunch
        
        m1 "중학생 때부터 쭉 누나만을 좋아했어요.. 제가 어떤 사람이어도 누나는 절 사랑해 주실 거 같다는 생각이 들어요."

        label goback:
        m1 "저랑 사귀어 주세요..!!"with vpunch

        menu:
            "너무나 당황스러운 고백.. 어떻게 하지? "

            "그래 나도 사실 널 좋아했어 우리 사귀자":
            
                jump love4

            "미안.. 난 지금이 좋아":

                jump ending4

label love4:
    scene background_happyEnding
    "이럴수가.. 오늘부터 1일!!"
    "{b}Happy Ending{/b}."

    menu:
        "다른 남자도 만나볼래!":
            jump choice
        "이대로 끝낼래요!":
            return

label ending1:

    "내가 대답을 잘 한 게 맞을까?"

    m1 "누나.. 너무해요!!"

    "{b}
    다시 잘 생각 해 봐!!\n
    Bad Ending{/b}."  with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump start1
        "남자 선택으로 돌아갈래요!":
            jump choice
        "아니요, 이대로 끝낼래요!":
            return

label ending2:
    "표정 관리가 안 되기 시작한다."
    
    m1 "누나 표정이 왜 그래요?.. 저랑 있는 게 부담스러워요?"

    "참고 먹다가 체 해!!"
    "{b}Bad Ending{/b}." with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump cafeteria
        "남자 선택으로 돌아갈래요!":
            jump choice
        "아니요, 이대로 끝낼래요!":
            return

label ending3:
    "말을 잘 들어줬어야지!!"

    "{b}Bad Ending{/b}." with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump playground
        "남자 선택으로 돌아갈래요!":
            jump choice
        "아니요, 이대로 끝낼래요!":
            return

label ending4:

    "다 왔는데 이런.. 눈치 좀 챙겨 [player_name]!!!"

    "{b}Bad Ending{/b}." with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump goback
        "남자 선택으로 돌아갈래요!":
            jump choice
        "아니요, 이대로 끝낼래요!":
            return


# 배진혁

label start2:
    p "아 오늘 체육 있었지..."

    "짝피구...? 내 짝은 누구지?"

    "배진혁...?"

label jin_love1:
    p "아야!"
    "발목을 삐었나..."
    m2 "아... 괜찮아? 같이 보건실 가줄게"

    "뭐라고 대답하지...?"
    menu:
        "아니야 괜찮아 혼자 갈게":

            jump jin_ending1

        "그래주면 고맙지!" :

            jump jin_love2

label jin_love2:
    scene background2_3
    "진혁이 부축을 해주며 보건실로 향했지만 보건선생님은 출장을 가셨는지 자리에 계시지 않는다"
    m2 "아... 선생님이 안 계시네."
    label sick:
    m2 "너만 괜찮으면 내가 치료해줄게."

    menu:
        "아... 아니 괜찮아.":
        
            jump jin_ending2
        
        "정말...? 그럼 부탁할게.":

            jump jin_love3

label jin_love3:
    scene background2_2
    m2 "[player_name], 혼자 못 걷겠지? 업혀. 교실까지 데려다 줄게."

    "너무 갑작스러운데..."
    menu:
        "아니야... 충분히 혼자 걸을 수 있어.":
        
            jump jin_ending3
        
        "아, 응...! 염치없지만 부탁할게.":

            jump jin_ending4

label jin_ending1:
    m2 "아... 그래."
    "진혁이는 멋쩍은듯 서있다 돌아가버렸다"
    "부탁했어야지!!"
    "{b}Bad Ending{/b}." with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump jin_love1
        "남자 선택으로 돌아갈래요!":
            jump choice
        "아니요, 이대로 끝낼래요!":
            return

label jin_ending2:
    m2 "아... 그래 미안."
    "어색한 공기가 흐른다..."
    "부탁했어야지!!"
    "{b}Bad Ending{/b}." with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump sick
        "남자 선택으로 돌아갈래요!":
            jump choice
        "아니요, 이대로 끝낼래요!":
            return

label jin_ending3:
    m2 "그래...? 내가 좀 과했나보네."
    "진혁은 어색하게 웃으며 운동장으로 돌아갔다"
    "부탁했어야지!!"
    "{b}Bad Ending{/b}." with hpunch

    menu:
        "이전으로 돌아갈래요!":
            jump jin_love3
        "남자 선택으로 돌아갈래요!":
            jump choice
        "아니요, 이대로 끝낼래요!":
            return

label jin_ending4:
    "그렇게 진혁이의 등에 업혀 교실까지 올라왔다..."
    "그 전부터 진혁이를 좋아했던 나는 이때를 기회로 용기를 내어본다."

    p "저... 진혁아."
    p "지금 이런 말 하는게 어떻게 들릴지 모르겠지만..."
    p "나, 오래 전부터 널 좋아해왔어."
    p "그러니까 우리... 사귈래?"

    "내 고백을 들은 진혁이는 귀가 빨개지고 고개를 푹 숙인다."
    m2 "응... 좋아."

    scene background_happyEnding
    "{b}Happy Ending{/b}."
    menu:
        "다른 남자도 만나볼래!":
            jump choice
        "이대로 끝낼래요!":
            return

# 지승현

label start3:
    "시험기간 도서관에서 침 흘리며 졸고 있는 [player_name]"
    "그때 전교 1등 지승현 선배가 다가와서 깨워준다."

    p "헉 감사합니다!"

label seng_love1:

    m3 "공부 중인 거 같던데 같이 공부할래?"

    "뭐라고 대답하지...?"
    menu:
        "바쁘실 것 같은데 저 혼자 알아서 할게요":

            jump seng_ending1

        "네..! 저도 전교1등 만들어주세요!" :

            jump seng_love2

label seng_love2:
    
    m3 "좋아 같이 공부하자"
    m3 "무슨 공부를 도와줄까?"

    menu:
        "html공부":
        
            jump seng_ending2
        
        "미술공부":

            jump seng_ending3

        "React공부":    

            jump seng_love3

label seng_love3:
    m3 "그래, 좋아!"
label graduation:
    scene background3_2
    "승현 선배의 졸업 당일"

    menu:
        "승현 선배에게 고백한다.":
        
            jump seng_ending4
        
        "승현 선배에게 it쇼에 놀러오라고 자신의 번호를 남긴다.":

            jump seng_love4

label seng_love4:
    scene background3_3
    "1년 뒤 3학년이 된 미림이의 it쇼 당일"
    "저 멀리서 꽃다발을 든 승현이 걸어온다..."

    m3 "수고했어, [player_name]아(야)!"

    menu:
        "1년만에 본 승현선배에게 안기며 고백한다.":
        
            jump seng_ending6
            
        "감사합니다..!!!(부끄러워 한 뒤 도망친다)":

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
    "기초 다지고 다시 도전하자"
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