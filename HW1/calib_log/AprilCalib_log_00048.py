# AprilCalib log 48
# CalibRig::mode=2d
# @ Fri Dec  3 18:22:13 2021

from numpy import array
U=array([[431.0767822265625, 461.4186706542969, 401.4646606445312, 371.2070007324219, 491.7868347167969, 432.0941467285156, 520.9813842773438, 462.7808837890625, 402.1817321777344, 339.9562377929688, 492.5806274414062, 371.4962463378906, 432.9621276855469],
       [316.8372192382812, 346.9271545410156, 348.0982360839844, 380.3911437988281, 376.6864624023438, 378.7388305664062, 406.646240234375, 408.8575134277344, 411.390869140625, 413.5970764160156, 439.2057800292969, 444.9065856933594, 442.2018127441406]], dtype='float64');
Xw=array([[699.5044555664062, 699.5044555664062, 499.5044555664062, 299.5044555664062, 699.5044555664062, 499.5044555664062, 699.5044555664062, 499.5044555664062, 299.5044555664062, 99.50446319580078, 499.5044555664062, 99.50446319580078, 299.5044555664062],
       [299.5044555664062, 499.5044555664062, 299.5044555664062, 299.5044555664062, 699.5044555664062, 499.5044555664062, 899.5044555664062, 699.5044555664062, 499.5044555664062, 299.5044555664062, 899.5044555664062, 499.5044555664062, 699.5044555664062],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype='float64');
# After LM:
K=array([[641.5865384494066, 0, 315.2311721631045],
       [0, 640.6844672219731, 246.4188526245037],
       [0, 0, 1]], dtype='float64');
distCoeffs=array([-0.03979819298158511,
       -0.001663050205720934,
       0.004569970295494912,
       -0.004814548140114753,
       0], dtype='float64');
CovK=array([[0.06321802813806707, 0.06039227844566318, 0.01064052135523781, -0.0378339009070254, 8.466242058752387e-06, 0.0004553068996381343, -1.453667342475712e-05, 2.956194386265353e-06, -0.0008808430927175461],
       [0.06039227844567099, 0.06457160460077621, 0.01629990499315178, -0.0319381311916247, 3.25714107047102e-05, 0.0003920482597326814, -1.794730938633905e-05, 4.601748372093285e-06, -0.0007843031988804269],
       [0.01064052134924974, 0.01629990498666619, 0.2281176494797935, -0.004266387812190351, 2.441847289626027e-05, 0.0001739636709272758, -4.145344799381343e-06, 9.464088044733018e-05, -0.000479450049049463],
       [-0.03783390090633874, -0.03193813119128207, -0.004266387824725119, 0.1536668627617436, -9.275012597239318e-05, -4.446668437000978e-05, 6.008137718417832e-05, -4.513868409082327e-06, 0.0002591890679711703],
       [8.466242058519892e-06, 3.257141070469797e-05, 2.44184729089178e-05, -9.275012597128365e-05, 3.317746788401157e-06, -1.885551511135857e-05, -9.861353853203876e-08, 6.533351032780232e-09, 3.473962623423333e-05],
       [0.0004553068996337415, 0.0003920482597277027, 0.0001739636709416774, -4.446668436976379e-05, -1.885551511136263e-05, 0.0001281725259095336, 1.557897370661462e-07, 1.141449224930281e-07, -0.0002502435158878001],
       [-1.453667342445035e-05, -1.794730938616258e-05, -4.145344804137889e-06, 6.008137718398688e-05, -9.86135385323604e-08, 1.557897370665485e-07, 3.600906180929937e-08, -2.804729004694689e-09, -1.988318690077376e-07],
       [2.956194383785346e-06, 4.601748369414479e-06, 9.464088044732098e-05, -4.513868403943603e-06, 6.533351027303051e-09, 1.141449224895516e-07, -2.804729002757174e-09, 4.253507441411249e-08, -2.941745404442193e-07],
       [-0.0008808430927057542, -0.000784303198867764, -0.0004794500491090811, 0.0002591890679649971, 3.473962623424388e-05, -0.0002502435158878086, -1.988318690087179e-07, -2.941745404631052e-07, 0.0005072637278792033]], dtype='float64');
# rms=0.215172
r0=array([-0.3808083924001482,
       -0.004376564416574386,
       0.05165438572893531], dtype='float64');
t0=array([282.420682164529,
       -57.38447757686972,
       3247.184271954937], dtype='float64');
Covr0=array([[5.583454131888933e-07, -3.64878716852426e-08, -8.307624160676785e-08],
       [-3.648787171450996e-08, 9.783186552514458e-07, 5.677490251587491e-08],
       [-8.307624160963745e-08, 5.67749025122375e-08, 2.869305612276934e-08]], dtype='float64');
Covt0=array([[5.939197734654662, 0.003158261270509795, -0.4400188197692126],
       [0.003158260933581795, 3.899796698002317, 1.139958393437253],
       [-0.4400188200459745, 1.13995839343887, 1.919659048641239]], dtype='float64');
r1=array([-0.3710383504381799,
       0.1475942034066386,
       -0.08799491391730918], dtype='float64');
t1=array([-717.7500011960269,
       38.40730011204199,
       4387.368038861193], dtype='float64');
Covr1=array([[6.318095921649914e-07, 1.827248499885648e-08, 6.454839932136236e-10],
       [1.827248497652029e-08, 7.578549473471359e-07, 7.084943596781246e-08],
       [6.454839904079697e-10, 7.084943596641241e-08, 1.968259540140802e-08]], dtype='float64');
Covt1=array([[10.57828542921338, -0.1069283496674185, 0.961295870191082],
       [-0.1069283502336834, 7.190075649499694, 1.950347880813628],
       [0.9612958699574907, 1.950347880936001, 2.958718229630151]], dtype='float64');
r2=array([-0.03082223488168693,
       0.0007338273041083267,
       -0.1363490101058692], dtype='float64');
t2=array([-1021.227962501594,
       -48.04560499903224,
       3497.682744120484], dtype='float64');
Covr2=array([[9.40139128247495e-07, -4.027374483033993e-08, 1.858668994529337e-08],
       [-4.027374484597695e-08, 7.533199240272027e-07, -3.208370727625552e-08],
       [1.858668994603904e-08, -3.208370727605043e-08, 7.057742450030148e-09]], dtype='float64');
Covt2=array([[6.79484632664535, -0.06315409980013433, 1.118699009756128],
       [-0.06315410017658686, 4.713887108314995, 1.344850825423428],
       [1.118699009586807, 1.344850825494086, 2.751444948131073]], dtype='float64');
r3=array([-0.2235832617658821,
       -1.120263732119759,
       0.1196937862163482], dtype='float64');
t3=array([-660.8697625171749,
       -374.7780587113659,
       472.5751142182484], dtype='float64');
Covr3=array([[3.624865326488301e-07, 2.189951102576158e-08, -1.420852523239291e-07],
       [2.189951100028216e-08, 5.219851101952482e-07, 3.595278543224104e-08],
       [-1.420852523262098e-07, 3.595278541954663e-08, 9.430734629762146e-08]], dtype='float64');
Covt3=array([[0.1944053896637509, -0.01162715646418204, 0.05831050438397015],
       [-0.01162715647290443, 0.1281029563051158, 0.1582095536178292],
       [0.05831050436425367, 0.1582095536276054, 0.548672685559756]], dtype='float64');
r4=array([-0.2442301599029215,
       -0.877065740666337,
       0.1099438279273281], dtype='float64');
t4=array([-1274.279439237971,
       -210.2814973674649,
       1452.141016133373], dtype='float64');
Covr4=array([[4.316779329447093e-07, -3.6066868375006e-09, -8.016982075432137e-08],
       [-3.60668686887902e-09, 5.625839473017419e-07, 2.272025829482701e-08],
       [-8.016982075607738e-08, 2.272025828903342e-08, 5.381425875309321e-08]], dtype='float64');
Covt4=array([[1.517206333541696, -0.04110448861896044, 0.3988924002323763],
       [-0.04110448871001657, 1.027060510694879, 0.5905108947925006],
       [0.398892400063279, 0.5905108948313127, 1.776113952894696]], dtype='float64');
r5=array([1.044473079135311,
       -0.04690377274435337,
       -0.0587159178383714], dtype='float64');
t5=array([-1033.138822373405,
       -412.9490386559695,
       3156.667008131923], dtype='float64');
Covr5=array([[5.134718358433789e-07, 1.216173773052964e-08, -1.241180027570315e-08],
       [1.216173770284987e-08, 5.774701108917364e-07, -2.581526130415873e-07],
       [-1.241180026071794e-08, -2.58152613042885e-07, 1.677540622452247e-07]], dtype='float64');
Covt5=array([[5.615477272118289, -0.1371541005510404, 1.224048576137297],
       [-0.1371541008514669, 3.758348609876228, 1.26491903758388],
       [1.224048575907852, 1.264919037690321, 3.021349077124516]], dtype='float64');
r6=array([0.01830926904178532,
       -0.5850748913717536,
       -1.020728631155174], dtype='float64');
t6=array([-791.4584938231725,
       765.928181841297,
       2883.783966405785], dtype='float64');
Covr6=array([[4.929697793674827e-07, -9.263822729452545e-08, -6.516080256422962e-08],
       [-9.263822731926917e-08, 6.449380974152244e-07, -8.597288346582438e-08],
       [-6.51608025616524e-08, -8.597288347058323e-08, 4.234053048795918e-08]], dtype='float64');
Covt6=array([[4.858127010886895, -0.0145901580430617, 0.6150231922355578],
       [-0.01459015831182888, 3.241462717407857, 0.3174432717091125],
       [0.6150231921020428, 0.3174432717740953, 2.01680648447253]], dtype='float64');
r7=array([-0.8136935363822015,
       0.1546584677314412,
       0.09025447957589272], dtype='float64');
t7=array([-442.83252887564,
       348.1511522235721,
       3778.655477421794], dtype='float64');
Covr7=array([[3.741650970937127e-07, 1.898379711185412e-08, 1.53217457519842e-08],
       [1.898379708537339e-08, 5.269114756021073e-07, 1.596250567007009e-07],
       [1.532174574309876e-08, 1.596250567016321e-07, 6.082642917517623e-08]], dtype='float64');
Covt7=array([[7.872329663942772, -0.03807769872659313, 0.3656044806106968],
       [-0.0380776991580239, 5.382957097403155, 1.226312671425563],
       [0.3656044804098036, 1.226312671483241, 1.827820281773]], dtype='float64');
r8=array([-0.9795690482996051,
       0.314037108651699,
       0.4459645777344646], dtype='float64');
t8=array([-459.7373223046055,
       281.0140252284784,
       5091.193611713266], dtype='float64');
Covr8=array([[5.450533055772092e-07, -5.257213130156741e-09, 8.219928954410691e-08],
       [-5.257213158142419e-09, 6.427931219711361e-07, 2.185658359058583e-07],
       [8.219928953356214e-08, 2.185658359113806e-07, 1.275359675284252e-07]], dtype='float64');
Covt8=array([[14.24736850600083, -0.06062246097770915, 0.3850570676820285],
       [-0.06062246176011425, 9.914988866873548, 2.237885162718342],
       [0.3850570673345007, 2.23788516280231, 3.251984747148613]], dtype='float64');
r9=array([-0.5126970845128468,
       0.1195188586586192,
       1.387749311380044], dtype='float64');
t9=array([-1356.808188872489,
       -242.4624098756854,
       5049.847779765459], dtype='float64');
Covr9=array([[1.172827607567677e-06, 3.298326104307288e-07, 2.220504477495587e-07],
       [3.298326104057535e-07, 1.183876558789075e-06, -7.736990645651279e-08],
       [2.220504477495854e-07, -7.73699064493923e-08, 9.939950164041004e-08]], dtype='float64');
Covt9=array([[14.73008769010316, -0.5498906644069335, 0.9863406257281206],
       [-0.5498906651986707, 9.775555518845543, 3.318360089764383],
       [0.9863406251963247, 3.318360089918057, 5.455855986395708]], dtype='float64');
r10=array([-0.4170601541661539,
       -0.1375071452134619,
       -0.1561869521687713], dtype='float64');
t10=array([-1001.199677813435,
       670.5630268064867,
       5501.607717189421], dtype='float64');
Covr10=array([[6.771329306788747e-06, -1.568540894596272e-06, 4.340452229707874e-07],
       [-1.568540894613684e-06, 4.573107078131678e-06, -2.587002707062784e-07],
       [4.340452229689817e-07, -2.58700270713022e-07, 1.166643487056366e-07]], dtype='float64');
Covt10=array([[17.01192236311202, -0.3213156795294975, 0.6503977864336725],
       [-0.3213156805610472, 12.42916290114297, 4.85301332295461],
       [0.6503977856216501, 4.853013323082776, 13.2866401991146]], dtype='float64');
r11=array([0.5690796542873202,
       -0.08460333636611934,
       0.01764104830688077], dtype='float64');
t11=array([-974.1230156335132,
       565.9358913076526,
       4570.332978051751], dtype='float64');
Covr11=array([[1.186940706955712e-06, 3.018788465685501e-08, 4.185112211549788e-08],
       [3.018788463123992e-08, 9.543740062784262e-07, -3.483834779599164e-07],
       [4.185112212555343e-08, -3.483834779609974e-07, 1.885843181959325e-07]], dtype='float64');
Covt11=array([[11.7281008815874, -0.09618784505904798, 1.154002127192643],
       [-0.09618784570323342, 8.218541005569074, 2.297891776096245],
       [1.154002126881034, 2.297891776248759, 6.15151778754186]], dtype='float64');
r12=array([-0.3695329596221721,
       -0.9477380557077495,
       -0.1183560654606493], dtype='float64');
t12=array([-1299.005512371981,
       -32.59449191533158,
       752.4173715031822], dtype='float64');
Covr12=array([[6.381708294459061e-07, -4.06900064658649e-08, -8.738271347502172e-08],
       [-4.069000649163319e-08, 7.811387925068526e-07, 5.444825025775073e-08],
       [-8.738271347778267e-08, 5.444825024912177e-08, 1.001785918109385e-07]], dtype='float64');
Covt12=array([[0.9202324047002389, -0.08899313930013462, -0.1791562990422108],
       [-0.08899313932677584, 0.4830344038822739, 0.3450577179887826],
       [-0.1791562990811766, 0.3450577180198886, 1.836858677713032]], dtype='float64');
r13=array([-0.3540550963442581,
       1.00537248180397,
       -0.0314877881429016], dtype='float64');
t13=array([678.280781501779,
       224.886258919268,
       3185.752447918847], dtype='float64');
Covr13=array([[8.900552043978887e-07, 3.064502889047729e-08, -9.661210039341403e-08],
       [3.064502886682923e-08, 9.813311641376772e-07, -6.156894934770079e-08],
       [-9.661210039469079e-08, -6.156894933906214e-08, 2.187674554147877e-07]], dtype='float64');
Covt13=array([[5.82949866947092, 0.007576726140454483, -0.8605225209733184],
       [0.007576725819108471, 4.059428535457362, 1.365284770826376],
       [-0.8605225211827912, 1.365284770782822, 3.278699267857982]], dtype='float64');
r14=array([-0.8362057642751618,
       0.7795916182941991,
       1.172241767879779], dtype='float64');
t14=array([939.0472128763457,
       888.891111850158,
       4195.191526465304], dtype='float64');
Covr14=array([[7.971233824594208e-07, 1.315642715726432e-07, 2.30024233792744e-07],
       [1.315642715453692e-07, 9.81521122753252e-07, 1.069311536207296e-07],
       [2.30024233787736e-07, 1.069311536326917e-07, 1.589513346959409e-07]], dtype='float64');
Covt14=array([[10.01857100575723, -0.2967352510552748, -2.728217908598106],
       [-0.2967352516018101, 7.177676981974082, 1.567785482660066],
       [-2.72821790881888, 1.567785482566091, 4.077076394019961]], dtype='float64');
r15=array([-1.096898157992115,
       0.4842484886317496,
       0.5243557109416181], dtype='float64');
t15=array([1705.457757837864,
       622.0011984732869,
       4006.093068619559], dtype='float64');
Covr15=array([[8.362720460507381e-07, -4.37104841418329e-08, 1.442137451444497e-07],
       [-4.371048416541829e-08, 1.507699953962303e-06, -2.087122125058334e-07],
       [1.442137451330705e-07, -2.0871221250359e-07, 4.818900222783292e-07]], dtype='float64');
Covt15=array([[10.42945509415076, 0.1891619759673528, -1.306383493869405],
       [0.1891619754374589, 7.145332110324635, 3.212148726855877],
       [-1.306383494233106, 3.212148726665772, 12.76783745946485]], dtype='float64');
r16=array([-0.5741639179351111,
       0.8420739106408814,
       0.4786826924659568], dtype='float64');
t16=array([1028.82163115455,
       124.2365116263461,
       2855.322662909851], dtype='float64');
Covr16=array([[9.604522252395123e-07, -1.370424775637078e-07, 1.319086217582913e-07],
       [-1.370424775858393e-07, 1.262243798164343e-06, 2.288044632027521e-09],
       [1.319086217527079e-07, 2.288044639260294e-09, 1.490011278274776e-07]], dtype='float64');
Covt16=array([[4.739753069960218, -0.01183312696146387, -1.592299833733159],
       [-0.01183312722154235, 3.393476109013987, 1.197953433996239],
       [-1.592299833887417, 1.197953433929669, 2.567134605163865]], dtype='float64');
r17=array([0.04695411772847879,
       1.458851923663797,
       0.07994386882113143], dtype='float64');
t17=array([801.5497397895067,
       -124.6125215646427,
       2140.769895874659], dtype='float64');
Covr17=array([[6.425866228618845e-07, 6.233997188986424e-08, 2.364137902254275e-07],
       [6.233997186741889e-08, 7.926963126868492e-07, -3.088820538980182e-08],
       [2.364137902288707e-07, -3.088820537611304e-08, 1.830014985906554e-07]], dtype='float64');
Covt17=array([[2.793740558750575, -0.02193349560765871, -0.7315520074898548],
       [-0.02193349575754258, 1.884128920662348, 0.748991822927829],
       [-0.7315520075944371, 0.7489918228961162, 1.532288347432343]], dtype='float64');
r18=array([0.01539005131298586,
       1.404929899649123,
       -0.003207039933516574], dtype='float64');
t18=array([546.1561716509049,
       -79.82166317987335,
       2354.327531074054], dtype='float64');
Covr18=array([[3.467914493969659e-07, 4.012427766353622e-08, 1.465949070144919e-07],
       [4.012427764120543e-08, 5.466973682810387e-07, -3.267996906120714e-08],
       [1.465949070176033e-07, -3.267996904696337e-08, 1.337404936611123e-07]], dtype='float64');
Covt18=array([[3.158821151270294, -0.04823812417285199, -0.6506237951471463],
       [-0.04823812434054145, 2.111618366689463, 0.5912869186779859],
       [-0.6506237952367776, 0.5912869186560926, 0.8863937099032246]], dtype='float64');
r19=array([0.009091035505860014,
       1.228791797108666,
       -0.01128499817287016], dtype='float64');
t19=array([-272.8507940722752,
       8.409703955783129,
       2411.189574123831], dtype='float64');
Covr19=array([[4.012832154854032e-07, 3.503960334600629e-08, 1.136691731290776e-07],
       [3.503960332052819e-08, 5.860268104998983e-07, -3.379967584117486e-08],
       [1.136691731317807e-07, -3.379967582549823e-08, 1.751715185958666e-07]], dtype='float64');
Covt19=array([[3.221487831774895, -0.02078530711452355, 0.2332478907429966],
       [-0.02078530728405254, 2.120972053834009, 0.3395089166856928],
       [0.2332478906856583, 0.3395089167090423, 0.4407055196396087]], dtype='float64');
r20=array([-0.5157082213212303,
       -0.2506893986736905,
       0.03320398358705302], dtype='float64');
t20=array([-1555.753458991453,
       309.7296786507027,
       2056.326149191227], dtype='float64');
Covr20=array([[3.944067237074462e-06, 6.67328467869722e-07, 3.79679095346142e-07],
       [6.673284678471068e-07, 2.94635504742299e-06, 4.817294415474514e-08],
       [3.796790953414736e-07, 4.817294415412611e-08, 9.09452898488771e-08]], dtype='float64');
Covt20=array([[2.66780542861821, -0.1594005448687519, 0.6134437154569196],
       [-0.159400545014766, 2.182651319277759, 1.327572032252975],
       [0.6134437153642378, 1.327572032337893, 4.35041050711544]], dtype='float64');
r21=array([-0.4374254580027402,
       -0.9365394112619448,
       0.08867911153024173], dtype='float64');
t21=array([-1203.897377795773,
       -149.9126617358936,
       1378.475706059354], dtype='float64');
Covr21=array([[4.46919862880278e-07, 1.657598124026075e-08, -7.353679859114821e-08],
       [1.657598121275108e-08, 5.507939185454898e-07, 6.34094395806923e-08],
       [-7.353679859541661e-08, 6.340943957294103e-08, 8.105044141376393e-08]], dtype='float64');
Covt21=array([[1.368967514474609, -0.04988785159558289, 0.3559057351786898],
       [-0.04988785166619959, 0.9320476818572467, 0.5539409181149487],
       [0.3559057351038954, 0.5539409181594969, 1.562897761954606]], dtype='float64');
r22=array([-0.477677002179738,
       -0.9594523005745543,
       0.0006987548791116288], dtype='float64');
t22=array([-1328.162438723565,
       -73.57926433192193,
       1444.957202883721], dtype='float64');
Covr22=array([[5.224586578929172e-07, 4.021579157792975e-09, -7.262175034534623e-08],
       [4.021579132550409e-09, 6.269121613737859e-07, 6.669056750367622e-08],
       [-7.262175034969827e-08, 6.669056749494013e-08, 1.05152424555576e-07]], dtype='float64');
Covt22=array([[1.630954498197587, -0.1022048234735788, 0.2791965242631372],
       [-0.1022048235532593, 1.08666182576636, 0.6739338529555863],
       [0.2791965241819513, 0.673933853006944, 2.088903371559732]], dtype='float64');
r23=array([-0.5242368042832354,
       -0.1772710744973515,
       0.7519817189038299], dtype='float64');
t23=array([-601.2755978702862,
       -580.3041471429025,
       1976.694317489716], dtype='float64');
Covr23=array([[7.180521309333387e-07, 1.031314347459673e-07, 8.369680717729984e-08],
       [1.031314347225442e-07, 5.685900733187426e-07, 7.729882600148102e-08],
       [8.369680717239147e-08, 7.729882600106068e-08, 4.053723498966759e-08]], dtype='float64');
Covt23=array([[2.095891894541809, -0.04505870409412239, 0.255723157390057],
       [-0.04505870421019167, 1.465538585210198, 0.7858072917209741],
       [0.25572315729755, 0.7858072917487396, 1.073896523057304]], dtype='float64');
r24=array([-1.259114672035216,
       0.1900371446288904,
       0.04314119099093995], dtype='float64');
t24=array([-505.799900976811,
       481.0537365535042,
       3487.303431418834], dtype='float64');
Covr24=array([[3.608530338606767e-07, -6.177686875342778e-09, 2.081472858466338e-08],
       [-6.177686899724095e-09, 5.012266539401736e-07, 2.805481809625201e-07],
       [2.081472857006353e-08, 2.805481809636047e-07, 1.767447927378784e-07]], dtype='float64');
Covt24=array([[6.799353075884268, 0.0196760903240483, 0.5674445382237391],
       [0.01967608996112499, 4.574357375451108, 0.732012640868404],
       [0.5674445380869173, 0.732012640926587, 1.260008923424155]], dtype='float64');
r25=array([-0.9173617535345823,
       0.1175335858479522,
       0.1253044441183702], dtype='float64');
t25=array([-661.6458493423007,
       230.6614899465887,
       3305.374899899013], dtype='float64');
Covr25=array([[3.500210548008282e-07, 2.943745387568041e-08, 3.014488826887422e-08],
       [2.943745384951241e-08, 5.051914556603334e-07, 1.880921795463256e-07],
       [3.014488825858758e-08, 1.880921795477318e-07, 7.963655667144217e-08]], dtype='float64');
Covt25=array([[5.988807275537675, -0.01848962859692647, 0.741726011887217],
       [-0.01848962892666661, 4.12897488107902, 0.9620533782723306],
       [0.7417260117335681, 0.9620533783403046, 1.446982436420195]], dtype='float64');
r26=array([-0.2439240750021895,
       -0.02439937243785219,
       0.10628397689882], dtype='float64');
t26=array([-806.3723835883054,
       -556.1493969099714,
       3003.178390536161], dtype='float64');
Covr26=array([[5.534619255499195e-07, 2.877902186838989e-08, 8.685579546644724e-09],
       [2.877902184186167e-08, 5.798313684619035e-07, 5.978774189244398e-08],
       [8.685579543392609e-09, 5.978774189235068e-08, 1.056965725853777e-08]], dtype='float64');
Covt26=array([[4.995172961435909, -0.1095000346597233, 0.7675272399549745],
       [-0.109500034936354, 3.392062033949335, 1.411497675030371],
       [0.7675272397616609, 1.411497675100443, 2.074690214846508]], dtype='float64');
r27=array([-0.9004036529156025,
       0.1398753061983424,
       -0.1532452866336999], dtype='float64');
t27=array([-1607.028234782626,
       651.7645470060208,
       5111.092535323918], dtype='float64');
Covr27=array([[1.629994136892758e-06, -2.382297460176364e-07, 4.82363712280084e-08],
       [-2.382297460435437e-07, 1.643053146230579e-06, 4.338655960791975e-07],
       [4.823637121835725e-08, 4.338655960816647e-07, 1.82115969704817e-07]], dtype='float64');
Covt27=array([[15.00465022742415, 0.3146386632347664, 3.458758486310215],
       [0.3146386624298956, 10.92931519400136, 2.493106406620863],
       [3.458758485939883, 2.493106406876128, 5.448770834737697]], dtype='float64');
r28=array([-0.8807182616616507,
       0.1436337324102777,
       1.268212349166696], dtype='float64');
t28=array([-1231.820320700013,
       509.4494588156365,
       5591.45597499458], dtype='float64');
Covr28=array([[1.900263331912587e-06, 1.736848878673203e-07, 4.319275214119554e-07],
       [1.73684887842067e-07, 1.560130659618837e-06, -6.67165601315686e-08],
       [4.319275214048846e-07, -6.671656012428961e-08, 2.363192959491589e-07]], dtype='float64');
Covt28=array([[17.76453254770026, -0.668785180884812, 0.9933109896023604],
       [-0.668785181856545, 12.52928848866982, 3.323168557308651],
       [0.9933109890667585, 3.323168557479232, 6.466326257784631]], dtype='float64');
r29=array([-0.9971278975762983,
       0.3252208810489602,
       1.38881854871328], dtype='float64');
t29=array([-1097.68102066688,
       591.4633093291991,
       6045.714835135715], dtype='float64');
Covr29=array([[1.43419324361986e-06, 1.541291252295027e-07, 4.360085298995454e-07],
       [1.541291252024792e-07, 1.552943779025697e-06, -9.040498195670397e-08],
       [4.36008529891834e-07, -9.040498194602009e-08, 3.263355665712176e-07]], dtype='float64');
Covt29=array([[20.76737263432755, -0.6661898657076415, 0.6151667133240089],
       [-0.6661898668223417, 14.56416633075038, 3.568630815806588],
       [0.6151667127611761, 3.568630815972601, 7.635375553605535]], dtype='float64');
r30=array([-0.5623049137227889,
       0.4278736796484006,
       0.7803602473788781], dtype='float64');
t30=array([1306.745725957532,
       434.8978359698116,
       6151.441011215067], dtype='float64');
Covr30=array([[4.698609087916876e-06, -6.654597495179976e-08, -1.474676868727494e-07],
       [-6.654597497656857e-08, 4.456082363219222e-06, -2.057660192176727e-07],
       [-1.474676868776178e-07, -2.057660192119428e-07, 2.257753049788679e-07]], dtype='float64');
Covt30=array([[22.49320782376556, 0.818815882039404, -2.471558516088586],
       [0.8188158808780942, 16.79324732283683, 7.157462208076622],
       [-2.47155851680661, 7.157462207826545, 14.97135994309122]], dtype='float64');
r31=array([-0.2781712472765443,
       0.3011673971905244,
       0.5725601886008163], dtype='float64');
t31=array([1098.544516294038,
       50.20802836503334,
       5273.062491700682], dtype='float64');
Covr31=array([[2.240114807292506e-06, -1.185495391551873e-08, -3.466863297638658e-07],
       [-1.185495394204078e-08, 1.969020954845433e-06, -7.082192522872643e-09],
       [-3.466863297665728e-07, -7.082192523740424e-09, 8.225446797767457e-08]], dtype='float64');
Covt31=array([[15.86482723646181, -0.01129935411126968, -2.880623374389093],
       [-0.01129935497532254, 10.63125447138156, 3.262777971534257],
       [-2.880623374906322, 3.262777971448545, 6.213158025736002]], dtype='float64');
r32=array([-0.7018353434783731,
       0.08748792735232082,
       1.648499405596622], dtype='float64');
t32=array([-466.5617371946989,
       -163.4535611366356,
       3201.044416281845], dtype='float64');
Covr32=array([[1.11334135320547e-06, 9.685162298293661e-08, 2.585366634407754e-07],
       [9.685162295482331e-08, 1.019247491894052e-06, -2.390412968538438e-08],
       [2.585366634355546e-07, -2.390412967695688e-08, 1.144717510499539e-07]], dtype='float64');
Covt32=array([[5.7516253665278, -0.2194511960966029, -0.05933657525092326],
       [-0.2194511964087538, 3.829762806403803, 1.318673293676014],
       [-0.05933657544755996, 1.318673293707298, 1.863990927345597]], dtype='float64');
r33=array([-0.2854762683893181,
       0.137196810082319,
       1.947536397856594], dtype='float64');
t33=array([-54.5448660468042,
       -123.8460383793282,
       1510.318679643927], dtype='float64');
Covr33=array([[4.255805278472698e-06, 6.172722074330399e-08, 5.331401847997271e-07],
       [6.172722069959161e-08, 1.976463224548849e-06, -2.398665551696926e-07],
       [5.331401848016182e-07, -2.398665551611169e-07, 1.412284463632464e-07]], dtype='float64');
Covt33=array([[1.326571023992193, -0.03287417281706431, -0.2297138391572239],
       [-0.03287417288695463, 0.8389856749993627, 0.2992231150418115],
       [-0.2297138392010635, 0.2992231150390658, 0.703398401421621]], dtype='float64');
r34=array([-1.808800391283778,
       0.2608377772037258,
       2.479577583437446], dtype='float64');
t34=array([-692.0235267214847,
       1020.69303309165,
       2573.334164291728], dtype='float64');
Covr34=array([[9.683426421019231e-07, -2.070330334425219e-08, 6.332091990027183e-07],
       [-2.070330338967782e-08, 1.073356122588803e-06, 1.271129112742312e-07],
       [6.332091989914147e-07, 1.271129113059447e-07, 5.184043841279734e-07]], dtype='float64');
Covt34=array([[4.192385076506085, 0.02995148732175713, 0.1377271016557489],
       [0.02995148710411568, 2.592478268005176, -0.1323230952370404],
       [0.1377271015974804, -0.1323230952051505, 1.311598563418558]], dtype='float64');
r35=array([-1.766411524486658,
       0.4994087461091342,
       2.497159993362889], dtype='float64');
t35=array([55.19319234885327,
       855.3505038889239,
       3328.661714127877], dtype='float64');
Covr35=array([[7.873268795450269e-07, -1.028655667586187e-07, 6.011159492309145e-07],
       [-1.028655668046837e-07, 7.298218358476287e-07, 8.043257582118421e-08],
       [6.011159492193558e-07, 8.043257585865981e-08, 5.266867768469719e-07]], dtype='float64');
Covt35=array([[6.25586667792104, -0.08443936376148461, -0.7206845507483479],
       [-0.08443936409219736, 4.019373977424596, -0.2096865896619248],
       [-0.7206845508126267, -0.2096865896774159, 0.9975613449786472]], dtype='float64');
r36=array([1.916092168042905,
       -0.3233318791036253,
       -2.443088373444139], dtype='float64');
t36=array([-125.87337483882,
       982.1118492301157,
       3721.671841646544], dtype='float64');
Covr36=array([[9.559070046231912e-07, 1.880946580025667e-07, 5.738869803101495e-07],
       [1.880946579594831e-07, 6.952969394692488e-07, -2.537396887141341e-07],
       [5.738869803379943e-07, -2.53739688681951e-07, 6.099179326760733e-07]], dtype='float64');
Covt36=array([[7.919903869535394, -0.036072978802642, -0.5233987650283305],
       [-0.03607297921810704, 5.088972502421234, -0.3239465961274349],
       [-0.5233987651073547, -0.3239465961280787, 1.21620571721144]], dtype='float64');
r37=array([2.010760202413415,
       -0.3360997186587269,
       -2.383335988983317], dtype='float64');
t37=array([-107.1673692293145,
       962.8673922805141,
       3737.103317579388], dtype='float64');
Covr37=array([[1.559651776215127e-06, 5.740567162802701e-07, 1.010070115470692e-06],
       [5.740567162384309e-07, 1.627056569224103e-06, -3.999397575260614e-07],
       [1.010070115500551e-06, -3.999397574918595e-07, 1.343578278496797e-06]], dtype='float64');
Covt37=array([[8.928294591612321, 0.01513333808078555, -0.7590738123757967],
       [0.0151333376615267, 5.875094417444713, -0.8676790333092701],
       [-0.7590738124444758, -0.8676790333093211, 1.930287853877975]], dtype='float64');
r38=array([-1.136878665637935,
       1.167309005433882,
       1.277339152923168], dtype='float64');
t38=array([500.3963443294052,
       766.0064726579329,
       4074.663675922668], dtype='float64');
Covr38=array([[4.530153498591668e-07, 9.675669406415225e-08, 3.323413825003847e-07],
       [9.675669403158907e-08, 6.340639091515831e-07, 1.178728821669584e-07],
       [3.323413824947072e-07, 1.178728821919963e-07, 3.182522657409595e-07]], dtype='float64');
Covt38=array([[9.411034806674055, -0.2531380621361405, -1.653056051817737],
       [-0.253138062660051, 6.315334789015437, 0.6064588950671125],
       [-1.653056051967327, 0.6064588950190347, 1.733610082516273]], dtype='float64');
r39=array([-1.042242348733535,
       1.08674102458893,
       1.274095026179241], dtype='float64');
t39=array([512.502937010416,
       621.3127833492846,
       4164.822445750678], dtype='float64');
Covr39=array([[4.315262462483403e-07, 9.462021182665456e-08, 2.839596014401148e-07],
       [9.462021179943592e-08, 5.667616655296896e-07, 1.168649184470856e-07],
       [2.839596014355769e-07, 1.168649184656621e-07, 2.440050438509809e-07]], dtype='float64');
Covt39=array([[9.666121380942544, -0.255840369524194, -1.698224550233967],
       [-0.2558403700392677, 6.545535969436891, 0.9037793616752231],
       [-1.698224550409109, 0.903779361626996, 1.883867624655675]], dtype='float64');
r40=array([-1.058456025112342,
       1.138714331053064,
       1.347881124715646], dtype='float64');
t40=array([388.5565005850239,
       615.1406618270452,
       4273.73702973793], dtype='float64');
Covr40=array([[5.551091789098888e-07, 1.120038004018073e-07, 3.57748490746906e-07],
       [1.120038003742481e-07, 7.408704793709047e-07, 8.521892830436511e-08],
       [3.57748490743487e-07, 8.521892832500679e-08, 3.355419707428594e-07]], dtype='float64');
Covt40=array([[10.31155120450786, -0.2524230845783433, -1.592348172376796],
       [-0.2524230851186043, 7.008117803320854, 0.9358597420887087],
       [-1.592348172556643, 0.9358597420507599, 2.158794717904056]], dtype='float64');
r41=array([-0.6932746941121599,
       0.7918107383560237,
       1.397546927663605], dtype='float64');
t41=array([593.2922560529255,
       650.3385620327149,
       5352.39143009179], dtype='float64');
Covr41=array([[8.504654219029954e-07, 1.722207114438247e-07, 2.09383547184166e-07],
       [1.722207114125578e-07, 8.842044004244421e-07, -1.747028108978987e-08],
       [2.093835471822537e-07, -1.74702810767652e-08, 1.594607595281174e-07]], dtype='float64');
Covt41=array([[15.89561892358674, -0.4251602907659913, -2.736447435946502],
       [-0.4251602916384818, 11.12965663146255, 2.558554457839626],
       [-2.736447436333913, 2.558554457774259, 5.093751279644966]], dtype='float64');
r42=array([-0.584390610773826,
       0.5065714209378673,
       0.140269290772037], dtype='float64');
t42=array([1609.51807140063,
       535.8226074341571,
       5703.868569116819], dtype='float64');
Covr42=array([[1.568603123999586e-06, 4.390215871670726e-08, -3.805585942745901e-07],
       [4.390215869472645e-08, 1.869759301354674e-06, -2.187807297024955e-08],
       [-3.805585942814625e-07, -2.187807296873885e-08, 2.280214153513802e-07]], dtype='float64');
Covt42=array([[18.43304671068529, -0.07623596189153627, -5.16536319434693],
       [-0.07623596290775078, 13.10788959753291, 4.525650051251078],
       [-5.165363194943577, 4.525650051011501, 11.29351668129942]], dtype='float64');
r43=array([-0.2025123731327021,
       0.6349982833980159,
       -0.09798949477917125], dtype='float64');
t43=array([-920.4976101212909,
       364.4636947840268,
       5134.209316398229], dtype='float64');
Covr43=array([[5.120547862950754e-07, -5.781880951460359e-08, 1.048800806241423e-07],
       [-5.781880953949885e-08, 7.367698759241596e-07, -2.367411695164564e-09],
       [1.048800806236626e-07, -2.367411686135152e-09, 6.377876703190787e-08]], dtype='float64');
Covt43=array([[14.69377452684446, 0.06735022221497465, 1.49635001566625],
       [0.06735022142014321, 9.941162638647379, 1.969947584246126],
       [1.496350015294501, 1.969947584393669, 3.790879778849751]], dtype='float64');
r44=array([-0.2705697676413598,
       -0.6588666832619685,
       0.1214607970852401], dtype='float64');
t44=array([-1283.218314902954,
       122.3372275395954,
       4247.540884364165], dtype='float64');
Covr44=array([[5.680653985306833e-07, 3.508048727173142e-08, -4.892781290625569e-08],
       [3.50804872451741e-08, 6.357227546676756e-07, 1.969084180931673e-08],
       [-4.892781290800994e-08, 1.969084180337985e-08, 4.417471147556384e-08]], dtype='float64');
Covt44=array([[10.43742353643047, -0.1643415304899942, 0.9387860341437506],
       [-0.1643415310648366, 7.124175297404499, 2.138106009241513],
       [0.9387860337758421, 2.138106009370818, 4.664668233241263]], dtype='float64');
r45=array([-0.6533937110784018,
       0.7174118239843036,
       0.5907780799620528], dtype='float64');
t45=array([914.4979575558381,
       339.1039980265466,
       4503.077897530238], dtype='float64');
Covr45=array([[5.872283487838306e-07, 3.293682087123308e-08, 9.571557412580252e-09],
       [3.293682084807931e-08, 8.959999484613582e-07, 1.313108950272395e-07],
       [9.571557407058606e-09, 1.313108950345188e-07, 1.045837670144214e-07]], dtype='float64');
Covt45=array([[11.29986996211426, -0.09470244595552474, -2.655968730059706],
       [-0.09470244657588812, 7.890049998482897, 2.221724973016075],
       [-2.655968730382144, 2.221724972927567, 4.139200777378303]], dtype='float64');
r46=array([-0.8636450979429904,
       0.1894282924711782,
       0.1750695637038646], dtype='float64');
t46=array([-1093.445362741881,
       606.0125261259816,
       4477.945047728789], dtype='float64');
Covr46=array([[6.54514745192714e-07, 1.454968860916112e-08, 3.849915974181531e-08],
       [1.454968858378626e-08, 7.501215360342619e-07, 1.724304425338214e-07],
       [3.849915973347168e-08, 1.724304425372069e-07, 8.192572511683877e-08]], dtype='float64');
Covt46=array([[11.10843124278937, 0.03504794161577096, 1.722327886711033],
       [0.03504794100384044, 7.874961253767722, 1.585867823663742],
       [1.722327886435052, 1.585867823810675, 3.160166013824598]], dtype='float64');
r47=array([-0.3643453499068383,
       0.3268336586770175,
       1.217239862335015], dtype='float64');
t47=array([368.9334207647401,
       -51.82303216370362,
       5295.866255462989], dtype='float64');
Covr47=array([[2.441532924182085e-06, 6.054339636854645e-07, -1.185023194475033e-07],
       [6.054339636540706e-07, 2.499465455308161e-06, -2.811480110593423e-07],
       [-1.185023194493705e-07, -2.811480110542614e-07, 1.033444155706766e-07]], dtype='float64');
Covt47=array([[15.33502637991586, -0.3256271574335986, -2.16127975811479],
       [-0.3256271582856949, 10.69375693170337, 3.610275906171916],
       [-2.161279758609072, 3.610275906137461, 5.930097377363208]], dtype='float64');
r48=array([-0.005284958337355467,
       -0.1300081268183453,
       -0.7903819821951228], dtype='float64');
t48=array([-170.1498475448053,
       602.6793944434365,
       2821.469811352498], dtype='float64');
Covr48=array([[1.815224310376403e-06, 3.25730100135582e-07, -7.285159171356769e-08],
       [3.257301001118345e-07, 2.217200689419438e-06, -3.420143034693512e-07],
       [-7.285159170970158e-08, -3.420143034723971e-07, 9.413513311140162e-08]], dtype='float64');
Covt48=array([[4.571710856123614, 0.05908864702010531, 0.3507039888378827],
       [0.05908864677304465, 3.058761017085962, 0.6761954010268769],
       [0.3507039887319061, 0.6761954010609553, 2.970404982930313]], dtype='float64');
