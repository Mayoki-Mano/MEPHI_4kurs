# Загрузка массива из файла
import pickle
import re


def extract_words(text):
    # Находим все слова, состоящие из букв
    words = re.findall(r'\b\w+\b', text)
    return words

def filter_bad_text(array_of_texts):
    result = []
    unique_words2 = []
    count_words2 = {}
    for text in array_of_texts:
        words=extract_words(text[0])
        word1, word2, word3, word4 = words

        if word1 in {'есмь', 'есгь', 'усти', 'унию', 'апоф', 'укаю', 'обещ', 'удою', 'лунц', 'угрю', 'ухою',
               'анри', 'анфи', 'амию', 'ивою', 'отсю', 'опиш', 'одеж', 'урча', 'урда','елью','ублю','охрю',
                     'урда','андр','упре','евши','акхи','авди','арфу','инку','муфт','опре','емки','азям','амру','улье','удят','иргу','утре',
                     'одре','окре','анге','акру','иску','испу','акре','акте','емка','адми','усме','оспе','умре','орше','успе','афер','акту','еван','осте','удит','окне',
                     'муст','умни','орте','угле','умчи','ежил','исту','одне','инке','обще','объе','урке','опёр','арбу','осве','авне','всюд','инте','ушке','акын','ирге','азол','обде','обре','акое',
                     'умир','адре','утри','опит','епан','убыт','опус','обве','адуе','инка','ежит','азом','ливм','вскр','арчу','учре','иска','урчи','утаи','арен','укат','овце','апис','врем','врём',
                     'инда','арин','илот','унте','удои','ешил','исая','обме','овсе','афри','рват','ушат','арес','евпл','алчу','урия','ирга','можт','агор','астр','твер','встр','ерал','анжу','икну',
                     'опас','одар','одёр','туер','трюм','исай','астл','рожд','охре','удое','укис','ером','ефим','арфы','испы','услы','идеа','роят','ария','мясн','нкер','усер','азид',
                     'игна','арти','урки','ушми','авен','лаун','мигн','мирн','роит','анис','мавр','амил','искл','кайл','кашл','купл','азур','угре','инде','убое','оные','масл',
                     'истя','ахти','ерам','арми','архи','арчи','рифт','анус','ивам','тобе','тоге','токе','толе','торе','тоще','узле','инст','твор','капл','иско','испо','исхо',
                     'укра','ухни','искр','муар','ильм','удим','тоне','топе','амон','овит','омёт','мэтр','раск','юрок','колп','корп','арбы','индо','исче','ртын','важн','окат','авст','акут','имет',
                     'упас','испр','шутл','алек','анек','судк','сумк','сурк','сутк','ахну','окая','освя','алья','обры','исто','озве','отде','отпе','отре','отсе','изве','изде','изне','иске','томе','ибра',
                     'амин','афон','скин','летн','учен','ушан','обит','обст','офит','умор','яток','утом','екну','опия','опья','укая','анто','имхо','успо','отве','тузе','туне','узде','изра','убра',
                     'капы','обыч','укло','усто','очне','арке','арте','арфе','архе','арче','дале','изда','согн','солн','сомн','верн','весн','вечн','видн','вишн','вран','леон','личн','лишн','казн','качн',
                     'найт','нарт','никт','ничт','люфт','урат','хорт','набр','накр','свер','вздр','забр','запр','енол','игол','накл','насл','вязл','шерл','аким','туям','кошм','осып','амия','орты',}:
            continue
        if word2 in {'жу', 'ча', 'ша', 'ши', 'фи', 'мю', 'ол', 'гр', 'ca', 'ам', 'аз', 'эф', 'шп', 'шм', 'еф', 'жр','Ир', 'ка',
                'кл', 'кн', 'ож', 'бр', 'эп', 'тр', 'др', 'бр', 'пл', 'зл', 'тр', 'бл', 'эт', 'шл', 'ил', 'сл','фл', 'вс',
                'па', 'гл', 'дн', 'бь', 'хл', 'св', 'сг', 'сж', 'сп', 'ст', 'сч', 'тв', 'уб', 'ув', 'уд', 'ут','вл', 'ур',
                'кр', 'ту', 'су', 'чу', 'пы', 'пу', 'ля', 'ле', 'ко', 'ды', 'ду', 'бя', 'бу', 'ва', 'вп', 'вт','дж', 'зн','ив', 'ов', 'ок', 'ос'
                     , 'ба', 'жа', 'ма', 'са', 'мо', 'ме', 'ве', 'тя', 'аз', 'ар', 'ам', 'ви', 'ан', 'ки', 'ат', 'ку', 'аф', 'би'
                     ,'гн','Дж','дз','ди','ид','ит','мн','пи','сд','си','см','сн','сх','уг','ул','ун','ух','ха','шт','юн','яг','ик','ин','ск','ук','шк','як','иж','пр','сб','уз'
                     ,'уп','хр','эр','юм','вз','вн','вх','зв','хв','вд','вр','дв','юр','ег','ед','ен','ер','кв','ср','Фе','фр','ше'
                     ,'лб','чт','вк','ях','гв','эк','яр','гд','зр','мл','пш','пь','съ','уч','цв','чл','чр','чь','лж','мр','од','оз','ом','оп','ор'
                     ,'сф','ть','эс','яб','ящ','ги','сц','тл','вм','вч','въ','шв','оф','оц','оч','ущ','яс','зд','ус','аг',
                     'ап','ав','тщ','га','кс','эн','ощ','гу','ех','жд','мч','нр','тк','зу','пс','пт','ри','ти','уш','ци','шу','му','ог','вш','Ев','еж','ох','сз','юз','ют','Ян','ву','дл','эм','юл','ял','ро','рт','кб','мб',
                     'ес','хи','пе','ре','ис','ям','сш','та','яв','аж','ак','лг','лу','ру','сю','вг','ош','те','гм','ев','де','бо','дм','жи','ла','ра','се',
                     'зо','сы','фо','ху','чи','ры','фа','ца','ми','ло','це','Ге','ще','ге','зе','бе','ах','вя','иг','ль','лю','тю','ке','мг','фе','юх','дю',
                     'Ио','ио','мя','пя','ую','ас','ны','щи','дя','ау','мс','хо','бю','ря','лы','аи','щу','гю','рю','уй','кх','уе','юс','кт','дь',
                     'цо','ся','тэ','иа','цы','юб','цу','зы','хе','аб','ие','яз','ян','зи','сё'
                     }:
            continue
        if word3 in {'вниду', 'тешка', 'тошна', 'чешка', 'нешто', 'вошка', 'союзе','лионе','ядоша','жеода','наори','неожи','неопи','ядови',
                     'заост','изобр','неопр','наотр','изойд','адову','алому','еложу','жеоду','алеко','обета','обеща','отека','отела','женив'
                     ,'обним','отним','поним','понед','ейная','линуя','чения','заноч','обнаж','литах','нетях','нитах','футах','высчи','высши','жести'
                     , 'насти','высун','постр','имаго','ужало','ужасо','неудо','выеха','поеди','умета','ужели','ёжило','алеют','элеат','доеха'
                     , 'затво','алеши','елико','поена','обегу','алеут','умейн','отаву','изумр','соеди','обету','наибо','обуха','неуда','доена'
                     , 'выемк','отума','оберн','умает','умают','заинт','желто','онуфр','отару','обедн','наеди','обаче','неужт','умани','обидн',
                     'умаяв','тырло','обижа','заигр','ойкну','обила','вокру','отаре','закру','обаян','нильс','вояжу','ёжите','поите','воине','обухе','изюмо','отаве','ужасн','воите',
                     'литов', 'нилус','выкат','науще','онуче','появл','вотку','наудя','потир','наско','умаял','неизм','обухи','обучи','выуди','адуев',
                     'обаял', 'дотру', 'засто', 'насто','замир','обесп','отелу','умира','наибл','никло','фукса','помир','отуча','зауми','четыр','готув','футов','неско',
                     'закут','закип','изуча','обуян','вояжа','вояжи','оными','неизв','четна','литер','литам','нитам','несмо','жерло','накло','чемто','неист','выигр','онагр',
                     'ёжила','умали','неспо','черво','нукер','накип','нумер','онучи','заике','оникс','тынки','линёк','литав','затыл','затку','четку','жесто','често','желта','солда','желёз','нельз',
                     'закис', 'лимбу','нимбу','быдто','онуча','наяду','алычи','изыду','умиле','женщи','женск','вытян','листо','изред','зарыд','отрез','былин','токма','дамно','нимба',
                     'алунд', 'дояра','изыму','оберт','линек','нутка','вырин','отряс','нарыв','полба','облас','фуксе','обиня','женка','бытье','вытье',
                     'вольн', 'должн','фуляр','желуд','дальш','лимба','дамбу','дамку','дампу','обяза','пояти','донки','доньи','гонту','литка','потяг','ворса','горча',
                     'черва','бывша','нивка','мылка','толка','волен','полин','полун','долив','гольд','голяд','солку','донка','донца','понра','донги','гонад','понад','донгу','донку','донцу','литое','потре',
                     'четъи', 'четьи','вытас','нотис','футер','высмо','мысик','мысок','посек','посёк','засек','насек','высту','заслу','черто','нерка','норда','торба','жерла','портн','обрив',
                     'лирам','порем','нарду','нарту','тырлу','тырсу','былье','полна','желти','мылки','полис','полус','полир','залов','залпу','нелюб','облач','токае','алкен',
                     'мыкол', 'никол', 'ликам','нукая','фукая','намес','задро','выздо','отира','понге','сонме','сонце','тынке','гонта','донга','понга','донял','тыном',
                     'линем', 'линём', 'линям','донья','затон','вотум','дотам','нутом','потам','мыска','ческа','воскр','выстр','засту','насту','горби','зарин','фуран',
                     'зарит','номад','помад','недав','подтв','подхв','недоу','годку','непир','непор','поясн','обыкн','обычн','фугам','выбра','побла','побра','собра','дачно',
                     }:
            continue
        if word4 in {'апоф', 'туею', 'луню', 'хулю', 'амию', 'ларю', 'окош', 'подш', 'туях','муфт','муар','акал','утре','отъе',
                     'муст','рази','мавр','отре','акут','отде','шутл','отве','арат','сумр','дуэл','врыт','тобе','тоге','токе','тоще','отпе',
                     'рани','раже','разе','расе','зифе','ртын','супр','топе','торе','килу','кипу','ране','рапе','рати','раке','сисе','сияе','отме','чувс','буер','сумл','тоне','укат','забр',
                     'рабе','раде','нише','нище','сибе','сиге','запр','зилу','сине','окот','люфт','бобе','боке','сиде','отсе','дикт','бухт','зине','утке',
                     'блюм','одре','дист','удое','туер','гику','гиту','кине','кипе','деят','адуе','нюхе','шуги','буев','гину','чуни','жерт','нкер','евпл','вязл','нием','адре','гужи','омёт',
                     'нине','ниче','оспе','одне','жути','чужи','чуки','дерн','желт','купл','публ','орок','зину','томе','гибе','ниве','нике','осве','осте','будт','опис','усер','умир','азар',
                     'кашл','двул','кипы','гиде','гизе','кире','низе','ните','туже','туфе','рясе','рюше','муси','мучи','ксен','андр','устр','алчу','амру','зино','гике','тузе','сучи','мирн','амон','дурн','урат','рват',
                     'отмс','укис','капл','набл','нашл','азол','арам','разд','гуня','гифы','каже','кате','каче','гите','исче','умре','руже','руце','тубе','туле','туне','кива','кика','кипа','кифа','киша','нюха',
                     'рези','хари','акхи','луди','луни','муви','овин','рвен','глин','амин','можт','повт','подт','поит','пойт','полт','пост','нест','нечт','осот','окат','омет','опус','туес','звер','твер','одер','одёр','резв',
                     'насл','апок','опок','ливм','оном','оным','арид','ятку','мамб','робе','роге','роже','роке','росе','чохе','капе','сите','исте','усме','успе','руле','руте','рюхе','гига','гика','гита','рели','сери','сечи',
                     'хаки','лущи','лаун','мигн','журн','лапт','анат','кикс','отыс','гетр','взгл','зебу','зеву','зету','капы','килы','шуто','годе','гоже','каме','пюже','деба','дета','кила','рюха','рюша',
                     'наги','нази','наси','наци','начи','буги','бучи','акын''роит','завт','заст','ласт','вскр','встр','омер','одар','вздр','обер','обор','роил','собл','согл','сосл','сохл','сошл','напл','енол',
                     'раек','раёк','раск','всяк','арак','арык','шпек','мягк','разм','тайм','усум','аким','гурд','сужд','тогу','раду','ражу','раму','рапу','ращу','хозя','заня','лудя','луня','хуля','зины',
                     'омег','тотч','рябо','рядо','роме','лаге','лаже','лазе','лаке','ларе',}:
            continue
        if word4 not in unique_words2:
            unique_words2.append(word4)
            count_words2[word4] =0
        else:
            count_words2[word4] += 1
        result+= text
    sorted_keys = sorted(count_words2, key=lambda x: count_words2[x], reverse=True)
    for word3 in sorted_keys:
        print(f',\'{word3}\'', end='')
    print()
    for word3 in sorted_keys:
        print(f',\'{word3}\' {count_words2[word3]}',end='')
    print()
    print(len(unique_words2))
    return result


with open("unique_matches.pkl", "rb") as f:
    loaded_matches = pickle.load(f)
filtered_texts = filter_bad_text(loaded_matches)
# for text in filtered_texts:
#     print(text)
print("Количество уникальных совпадений в изначальном массиве:", len(loaded_matches))
print("Количество отфильтрованных уникальных совпадений в изначальном массиве:", len(filtered_texts))