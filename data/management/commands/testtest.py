from data.models import Combinations, Combinations_partner, Champion
from django.core.management.base import BaseCommand
from collections import Counter

def champData(name, how):
    champ = {
    "TFT8_Kaisa" : 
    {
        "name" : "카이사",
        "traits" : ["정찰단","별 수호자"]
    },
    "TFT8_Lux" : 
    {
        "name" : "럭스",
        "traits" : ["주문투척자","별 수호자"]
    },
    "TFT8_Kayle" : {
        "name" : "케일",
        "traits" : ["지하세계", "결투가"]
    },
    "TFT8_Poppy" : {
        "name" : "뽀삐",
        "traits" : ["기계유망주","엄호대"]
    },
    "TFT8_Galio" : {
        "name" : "갈리오",
        "traits" : ["민간인", "마스코트"]
    },
    "TFT8_Rell" : {
        "name" : "렐",
        "traits" : ["별 수호자","엄호대"]
    },
    "TFT8_Velkoz" : {
        "name" : "벨코즈",
        "traits" : ["위협"]
    },
    "TFT8_Nilah" : {
        "name": "닐라",
        "traits" : ["별 수호자", "결투가"]
    },
    "TFT8_Ashe" : {
        "name":"애쉬",
        "traits" : ["정찰단", "레이저단"]
    },
    "TFT8_Yasuo" : {
        "name":"야스오",
        "traits" : ["레이저단", "결투가"]
    },
    "TFT8_Senna" : {
        "name":"세나",
        "traits" : ["레이저단", "특등사수"]
    },
    "TFT8_Zed" : {
        "name":"제드",
        "traits" : ["결투가", "레이저단", "해커"]
    },
    "TFT8_Lulu" : {
        "name":"룰루",
        "traits" : ["선의", "기계유망주"]
    },
    "TFT8_Nunu" : {
        "name":"누누",
        "traits" : ["마스코트", "기계유망주"]
    },
    "TFT8_Yuumi" : {
        "name":"유미",
        "traits" : ["별 수호자", "선의","마스코트"]
    },
    "TFT8_Zoe" : {
        "name":"조이",
        "traits" : ["기계유망주","익살꾼","해커"]
    },
    "TFT8_Taliyah" : {
        "name":"탈리야",
        "traits" : ["별 수호자", "주문투척자"]
    },
    "TFT8_Sivir" : {
        "name":"시비르",
        "traits" : ["민간인", "특등사수"]
    },
    "TFT8_Gangplank" : {
        "name":"갱플랭크",
        "traits" : ["결투가","우세"]
    },
    "TFT8_WuKong" : {
        "name":"오공",  
        "traits" : ["메카: 프라임", "엄호대"]
    },
    "TFT8_Draven" : {
        "name":"드레이븐",
        "traits" : ["메카: 프라임", "에이스"]
    },
    "TFT8_Malphite" : {
        "name":"말파이트",
        "traits" : ["우세","마스코트"]
    },
    "TFT8_Nasus" : {
        "name":"나서스",
        "traits" : ["마스코트","동물특공대"]
    },
    "TFT8_Jinx" : {
        "name":"징크스",
        "traits" : ["동물특공대","익살꾼"]
    },
    "TFT8_Vayne" : {
        "name":"베인",
        "traits" : ["동물특공대","정찰단","결투가"]
    },
    "TFT8_MissFortune" : {
        "name":"미스포츈",
        "traits" : ["에이스","동물특공대"]
    },
    "TFT8_Chogath" : {
        "name":"초가스",
        "traits" : ["위협"]
    },
    "TFT8_Rammus" : {
        "name":"람머스",
        "traits" : ["위협"]
    },
    "TFT8_BelVeth" : {
        "name":"벨베스",
        "traits" : ["위협"]
    },
    "TFT8_AurelionSol" : {
        "name":"아우렐리온솔",
        "traits" : ["위협"]
    },
    "TFT8_Zac" : {
        "name":"자크",
        "traits" : ["위협"]
    },
    "TFT8_Mordekaiser" : {
        "name":"모데카이저",
        "traits" : ["에이스", "레이저단"]
    },
    "TFT8_Leblanc" : {
        "name":"르블랑",
        "traits" : ["자동방어체계", "해커","주문투척자"]
    },
    "TFT8_Sylas" : {
        "name":"사일러스",
        "traits" : ["동물특공대", "무법자"]
    },
    "TFT8_Camille" : {
        "name":"카밀",
        "traits" : ["자동방어체계","무법자"]
    },
    "TFT8_Ezreal" : {
        "name":"이즈리얼",
        "traits" : ["지하세계","정찰단"]
    },
    "TFT8_Sona" : {
        "name":"소나",
        "traits" : ["지하세계", "선의", "주문투척자"]
    },
    "TFT8_Ekko" : {
        "name":"에코",
        "traits" : ["별 수호자", "방패대","익살꾼"]
    },
    "TFT8_Sett" : {
        "name":"세트",
        "traits" : ["메카: 프라임", "엄호대"]
    },
    "TFT8_Janna" : {
        "name":"잔나",
        "traits" : ["민간인","기상캐스터","주문투척자"]
    },
    "TFT8_Urgot" : {
        "name":"우르곳",
        "traits" : ["위협"]
    },
    "TFT8_Syndra" : {
        "name":"신드라",
        "traits" : ["선의","별 수호자"]
    },
    "TFT8_Fiddlesticks" : {
        "name":"피들스틱",
        "traits" : ["위협","타락"]
    },
    "TFT8_Blitzcrank" : {
        "name":"블리츠크랭크",
        "traits" : ["자동방어체계", "싸움꾼"]
    },
    "TFT8_Renekton" : {
        "name":"레넥톤",
        "traits" : ["싸움꾼","레이저단"]
    },
    "TFT8_Vi" : {
        "name":"바이",
        "traits" : ["싸움꾼", "방패대","지하세계"]
    },
    "TFT8_LeeSin" : {
        "name":"리신",
        "traits" : ["선의","싸움꾼"]
    },
    "TFT8_Riven" : {
        "name":"리븐",
        "traits" : ["동물특공대", "싸움꾼", "엄호대"]
    },
    "TFT8_Jax" : {
        "name":"잭스",
        "traits" : ["메카: 프라임", "싸움꾼"]
    },
    "TFT8_Sejuani" : {
        "name":"세주아니",
        "traits" : ["싸움꾼", "레이저단"]
    },
    "TFT8_Soraka" : {
        "name":"소라카",
        "traits" : ["자동방어체계", "선의"]
    },
    "TFT8_Talon" : {
        "name":"탈론",
        "traits" : ["황소부대", "무법자"]
    },
    "TFT8_Fiora" : {
        "name":"피오라",
        "traits" : ["황소부대", "결투가"]
    },
    "TFT8_Annie" : {
        "name":"애니",
        "traits" : ["황소부대", "기계유망주", "주문투척자"]
    },
    "TFT8_Alistar" : {
        "name":"알리스타",
        "traits" : ["황소부대", "마스코트", "방패대"]
    },
    "TFT8_Viego" : {
        "name":"비에고",
        "traits" : ["황소부대", "무법자"]
    },
    "TFT8_Samira" : {
        "name":"사미라",
        "traits" : ["에이스", "지하세계","특등사수"]
    },
    "TFT8_Aphelios" : {
        "name":"아펠리오스",
        "traits" : ["황소부대", "특등사수", "병기고"]
    },
    "TFT8_Leona" : {
        "name":"레오나",
        "traits" : ["메카: 프라임", "무법자", "방패대"]
    },
    }
    if how == "name":
        return champ[name]["name"]
    elif how == "traits":
        return champ[name]["traits"]

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        
        """
        콤비네이션오브젝트 하나하나마다
        오브젝트하나의 id로 파트너 오브젝트 찾고
        콤비네이션 유닛 배열 - 파트너 유닛배열 -> 이게 하나의 객체
        조건문으로 콤비네이션 유닛배열이 콤비네이ㅕㄴ 유닛배열 이나 파트너 유닛배열 이랑 같고
        파트너 배열이 나머지 하나랑 같으면 count + 1
        아니면 새로운 객체 생성
        이런식으로 쭉쭉 만들어서
        통계 얻기

        """

        deck1s = Combinations.objects.all()
        decks = []
        decksString = []
        for deck1 in deck1s:
            deck2 = Combinations_partner.objects.filter(id = deck1.id)
            if not deck2:
                print("id 같은게 없습니다")
                return
            deck1_units = []
            deck2_units = []
            for unit in deck1.units:
                deck1_units.append(champData(unit["character_id"],"name"))
            for unit in deck2[0].units:
                deck2_units.append(champData(unit["character_id"],"name"))
            temp = [deck1_units, deck2_units]
            temp.sort()
            decks.append(temp)
            decksString.append(str(temp))
        #데이터 더 들어와야 의미있는 결과 얻을 듯