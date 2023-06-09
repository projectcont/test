# DEFINE THE DATABASE CREDENTIALS
dbconf=dict (
        user = 'rssp2020_experts',
        password = 'Ov9IqDv3exp2',
        host = 'VH286.sweb.ru',
        port = 3306,
        database = 'rssp2020_experts'
)

expl='Привет!  Инструкция к тесту: Этот вопросник предназначен для определения типичных способов поведения и личностных характеристик. Он состоит из 70 утверждений (вопросов), каждое из которых имеет два варианта ответа. Вам необходимо выбрать ОДИН. Все ответы равноценны, среди них нет "правильных" или "неправильных"! Поэтому не нужно "угадывать" ответ. Выберите ответ, который свойствен вашему поведению в большинстве жизненных ситуаций. Работайте последовательно, не пропуская вопросов. Отвечайте правдиво, если вы хотите узнать что-то о себе, а не о какой-то мифической личности.'
user_name_prompt="Введите ваше имя:"
user_email_prompt="Введите ваш email"
expl2='Начнём? Ответьте на 70 вопросов, обычно это занимает 3-5 минут.'

question_1 = '1. В компании (на вечеринке) Вы <br/>а) общаетесь со многими, включая и незнакомцев; <br/>б) общаетесь с немногими - Вашими знакомыми. '
question_2 = '2. Вы человек скорее <br/>а) реалистичный, чем склонный теоретизировать; <br/>б) склонный теоретизировать, чем реалистичный. '
question_3 = '3. По-вашему, что хуже: <br/>а) витать в облаках; <br/>б) придерживаться проторенной дорожки. '
question_4 = '4. Вы более подвержены влиянию <br/>а) принципов, законов; <br/>б) эмоций, чувств. '
question_5 = '5. Вы более склонны <br/>а) убеждать; <br/>б) затрагивать чувства.'
question_6 = '6. Вы предпочитаете работать <br/>а) выполняя все точно в срок; <br/>б) не связывая себя определенными сроками. '
question_7 = '7. Вы склонны делать выбор <br/>а) довольно осторожно; <br/>б) внезапно, импульсивно.'
question_8 = '8. В компании (на вечеринке) Вы <br/>а) остаетесь допоздна, не чувствуя усталости; <br/>б) быстро утомляетесь и предпочитаете пораньше уйти.'
question_9 = '9. Вас более привлекают <br/>а) здравомыслящие люди; <br/>б) люди с богатым воображением. '
question_10 = '10. Вам интересно <br/>а) то, что происходит в действительности; <br/>б) те события, которые могут произойти.'
question_11 = '11. Оценивая поступки людей, Вы больше учитываете <br/>а) требования закона, чем обстоятельства; <br/>б) обстоятельства, чем требования закона. '
question_12 = '12. Обращаясь к другим, Вы склонны <br/>а) соблюдать формальности, этикет; <br/>б) проявлять свои личные, индивидуальные качества. '
question_13 = '13. Вы человек скорее <br/>а) точный, пунктуальный; <br/>б) неторопливый, медлительный.'
question_14 = '14. Вас больше беспокоит необходимость <br/>а) оставлять дела незаконченными; <br/>б) непременно доводить дела до конца. '
question_15 = '15. В кругу знакомых Вы, как правило <br/>а) в курсе происходящих событий; <br/>б) узнаете о новостях с опозданием.'
question_16 = '16. Повседневные дела Вам нравится делать <br/>а) общепринятым способом; <br/>б) своим оригинальным способом.'
question_17 = '17. Предпочитаю таких писателей, которые <br/>а) выражаются буквально, напрямую; <br/>б) пользуются аналогиями, иносказаниями. '
question_18 = '18. Что Вас больше привлекает <br/>а) стройность мысли; <br/>б) гармония человеческих отношений. '
question_19 = '19. Вы чувствуете себя увереннее <br/>а) в логических умозаключениях; <br/>б) в практических оценках ситуаций. '
question_20 = '20. Вы предпочитаете, когда дела <br/>а) решены и устроены; <br/>б) не решены и пока не улажены.'
question_21 = '21. Как по-вашему, Вы человек, скорее <br/>а) серьезный, определенный; <br/>б) беззаботный, беспечный. '
question_22 = '22. При телефонных разговорах Вы <br/>а) заранее не продумываете все, что нужно сказать; <br/>б) мысленно репетируете то, что будет сказано. '
question_23 = '23. Как Вы считаете, факты <br/>а) важны сами по себе; <br/>б) есть проявления общих закономерностей. '
question_24 = '24. Фантазеры, мечтатели обычно <br/>а) раздражают Вас; <br/>б) довольно симпатичны Вам. '
question_25 = '25. Вы чаще действуете как человек <br/>а) хладнокровный; <br/>б) вспыльчивый, горячий. '
question_26 = '26. Как по-вашему, хуже быть <br/>а) несправедливым; <br/>б) беспощадным. '
question_27 = '27. Обычно Вы предпочитаете действовать <br/>а) тщательно взвесив все возможности; <br/>б) полагаясь на волю случая. '
question_28 = '28. Вам приятнее <br/>а) покупать что-нибудь; <br/>б) иметь возможность купить. '
question_29 = '29. В компании Вы, как правило <br/>а) первым заводите беседу; <br/>б) ждете, когда с Вами заговорят. '
question_30 = '30. Здравый смысл <br/>а) редко ошибается; <br/>б) часто попадает впросак. '
question_31 = '31. Детям часто не хватает <br/>а) практичности; <br/>б) воображения. '
question_32 = '32. В принятии решений Вы руководствуетесь скорее <br/>а) принятыми нормами; <br/>б) своими чувствами, ощущениями. '
question_33 = '33. Вы человек скорее <br/>а) твердый, чем мягкий; <br/>б) мягкий, чем твердый.'
question_34 = '34. Что, по-вашему, больше впечатляет <br/>а) умение методично организовать; <br/>б) умение приспособиться и довольствоваться достигнутым.'
question_35 = '35. Вы больше цените <br/>а) определенность, законченность; <br/>б) открытость, многовариантность. '
question_36 = '36. Новые и нестандартные отношения с людьми <br/>а) стимулируют, придают Вам энергии; б} утомляют Вас. '
question_37 = '37. Вы чаще действуете как <br/>а) человек практического склада; <br/>б) человек оригинальный, необычный. '
question_38 = '38. Вы более склонны <br/>а) находить пользу в отношениях с людьми; <br/>б) понимать мысли и чувства других. '
question_39 = '39. Что приносит Вам больше удовлетворения <br/>а) тщательное и всесторонне обсуждение спорного вопроса; <br/>б) достижение соглашения по поводу спорного вопроса. '
question_40 = '40. Вы руководствуетесь более <br/>а) рассудком; <br/>б) велениями сердца. '
question_41 = '41. Вам удобнее выполнять работу <br/>а) по предварительной договоренности; <br/>б) которая подвернулась случайно. '
question_42 = '42. Вы обычно полагаетесь <br/>а) на организованность, порядок; <br/>б) на случайность, неожиданность. '
question_43 = '43. Вы предпочитаете иметь <br/>а) много друзей на непродолжительный срок; <br/>б) несколько старых друзей. '
question_44 = '44. Вы руководствуетесь в большей степени <br/>а) фактами, обстоятельствами; <br/>б) общими положениями, принципами. '
question_45 = '45. Вас больше интересуют <br/>а) производство и сбыт продукции; <br/>б) проектирование и исследования. '
question_46 = '46. Что Вы считаете за комплимент <br/>а) *Вот очень логичный человек*; <br/>б) *Вот тонко чувствующий человек*. '
question_47 = '47. Вы более цените в себе <br/>а) невозмутимость; <br/>б) увлеченность. '
question_48 = '48. Вы предпочитаете высказывать <br/>а) окончательные и определенные утверждения; <br/>б) предварительные и неоднозначные утверждения. '
question_49 = '49. Вы лучше чувствуете себя <br/>а) после принятия решения; <br/>б) не ограничивая себя решениями. '
question_50 = '50. Общаясь с незнакомыми, Вы <br/>а) легко завязываете продолжительные беседы; <br/>б) не всегда находите общие темы для разговора.'
question_51 = '51. Вы больше доверяете <br/>а) своему опыту; <br/>б) своим предчувствиям. '
question_52 = '52. Вы чувствуете себя человеком <br/>а) более практичным, чем изобретательным; <br/>б) более изобретательным, чем практичным. '
question_53 = '53. Кто заслуживает большего одобрения - <br/>а) рассудительный, здравомыслящий человек; <br/>б) человек, глубоко переживающий. '
question_54 = '54. Вы более склонны <br/>а) быть прямым и беспристрастным; <br/>б) сочувствовать людям. '
question_55 = '55. Что, по-вашему, предпочтительней <br/>а) удостовериться, что все подготовлено и улажено; <br/>б) предоставить событиям идти своим чередом.'
question_56 = '56. Отношения между людьми должны строиться <br/>а) на предварительной взаимной договоренности; <br/>б) в зависимости от обстоятельств. '
question_57 = '57. Когда звонит телефон, Вы <br/>а) торопитесь подойти первым; <br/>б) надеетесь, что подойдет кто-нибудь другой. '
question_58 = '58. Что Вы цените в себе больше <br/>а) развитое чувство реальности; <br/>б) пылкое воображение. '
question_59 = '59. Вы больше придаете значение <br/>а) тому, что сказано; <br/>б) тому, как сказано. '
question_60 = '60. Вы в основном считаете себя <br/>а) трезвым и практичным; <br/>б) сердечным и отзывчивым. '
question_61 = '61. Что выглядит большим заблуждением <br/>а) излишняя пылкость, горячность; <br/>б) чрезмерная объективность, беспристрастность. '
question_62 = '62. Какие ситуации привлекают Вас больше <br/>а) регламентированные и упорядоченные; <br/>б) неупорядоченные и нерегламентированные. '
question_63 = '63. Вы человек, скорее <br/>а) педантичный, чем капризный; <br/>б) капризный, чем педантичный. '
question_64 = '64. Вы чаще склонны <br/>а) быть открытым, доступным людям; <br/>б) быть сдержанным, скрытным. '
question_65 = '65. В литературных произведениях Вы предпочитаете <br/>а) буквальность, конкретность; <br/>б) образность, переносный смысл. '
question_66 = '66. Что для Вас труднее <br/>а) находить общий язык с другими; <br/>б) использовать других в своих интересах. '
question_67 = '67. Чего бы вы себе больше пожелали <br/>а) ясности размышлений; <br/>б) умения сочувствовать. '
question_68 = '68. Что хуже <br/>а) быть неприхотливым; <br/>б) быть излишне привередливым. '
question_69 = '69. Вы предпочитаете <br/>а) запланированные события; <br/>б) незапланированные события. '
question_70 = '70. Вы склонны поступать скорее <br/>а) обдуманно, чем импульсивно; <br/>б) импульсивно, чем обдуманно.'

questions=[ 'нет',
question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10,
question_11, question_12, question_13, question_14, question_15, question_16, question_17, question_18, question_19, question_20,
question_21, question_22, question_23, question_24, question_25, question_26, question_27, question_28, question_29, question_30,
question_31, question_32, question_33, question_34, question_35, question_36, question_37, question_38, question_39, question_40,
question_41, question_42, question_43, question_44, question_45, question_46, question_47, question_48, question_49, question_50,
question_51, question_52, question_53, question_54, question_55, question_56, question_57, question_58, question_59, question_60,
question_61, question_62, question_63, question_64, question_65, question_66, question_67, question_68, question_69, question_70,
]