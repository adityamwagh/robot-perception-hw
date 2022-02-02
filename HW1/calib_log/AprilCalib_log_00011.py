# AprilCalib log 11
# CalibRig::mode=2d
# @ Fri Dec  3 18:20:40 2021

from numpy import array
U=array([[276.664794921875, 304.0813293457031, 221.1020050048828, 329.6235046386719, 303.3163452148438, 382.0147094726562, 249.2869873046875, 223.0909118652344, 196.6053161621094, 377.1938781738281],
       [334.8479919433594, 334.174560546875, 335.8221740722656, 354.30126953125, 354.9306945800781, 352.8591613769531, 356.1312255859375, 376.4500732421875, 376.90234375, 390.9957580566406]], dtype='float64');
Xw=array([[699.5044555664062, 899.5044555664062, 299.5044555664062, 1099.504516601562, 899.5044555664062, 1499.504516601562, 499.5044555664062, 299.5044555664062, 99.50446319580078, 1499.504516601562],
       [99.50446319580078, 99.50446319580078, 99.50446319580078, 299.5044555664062, 299.5044555664062, 299.5044555664062, 299.5044555664062, 499.5044555664062, 499.5044555664062, 699.5044555664062],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype='float64');
# After LM:
K=array([[636.5867461511118, 0, 328.6033658502988],
       [0, 635.3020728653339, 244.3553263502164],
       [0, 0, 1]], dtype='float64');
distCoeffs=array([-0.05964410587094325,
       0.01870677888807678,
       0.006300497901731529,
       0.0001739633856643587,
       0], dtype='float64');
CovK=array([[0.2093929582898042, 0.2029326050731112, 0.1182301912240232, -0.1272856401906068, 0.0002224711065683172, 0.0006380856759482526, -5.142318665458075e-05, 3.83096066391909e-05, -0.001557697093783505],
       [0.2029326050730705, 0.2074226871265085, 0.1172942185860219, -0.1226290108988713, 0.0002727517995906198, 0.0004675448979811664, -5.918549071681807e-05, 3.681121338819687e-05, -0.00130942118298512],
       [0.1182301912121845, 0.1172942185741908, 0.5739190701211245, -0.1207834012853568, 0.000138768050285424, 0.001332690753711967, -5.819333757891209e-05, 0.0002272415028662816, -0.003186068096637116],
       [-0.1272856402042025, -0.1226290109123656, -0.1207834013722221, 0.4456133494667358, -0.0003564121423346056, 1.583522479460887e-05, 0.0001818421786732208, -4.984842189138161e-05, 0.0005545751532299376],
       [0.00022247110657594, 0.0002727517995983373, 0.0001387680503553295, -0.0003564121423179828, 8.615362986284645e-06, -4.606115072730488e-05, -3.688746010777966e-07, 5.515334826491908e-08, 8.440756313403042e-05],
       [0.000638085675917867, 0.0004675448979500176, 0.001332690753620276, 1.583522494617996e-05, -4.606115072745162e-05, 0.0003063072504296688, 8.64566563630603e-07, 5.331246431607254e-07, -0.0005999615132225215],
       [-5.142318665973183e-05, -5.918549072193709e-05, -5.819333761446369e-05, 0.0001818421786708537, -3.688746010827531e-07, 8.645665635664178e-07, 1.033796140224012e-07, -2.448967245696451e-08, -1.289361044370782e-06],
       [3.830960663475383e-05, 3.681121338375345e-05, 0.0002272415028671962, -4.984842185736631e-05, 5.5153348237756e-08, 5.331246431975644e-07, -2.448967244306241e-08, 1.002612170082185e-07, -1.24533914734053e-06],
       [-0.001557697093730188, -0.001309421182929804, -0.003186068096567945, 0.0005545751528678906, 8.440756313435597e-05, -0.0005999615132228126, -1.289361044520403e-06, -1.245339147312866e-06, 0.001225687225090856]], dtype='float64');
# rms=0.186231
r0=array([-0.3844493047344715,
       -0.01788893382931736,
       0.04963394407055359], dtype='float64');
t0=array([215.1788482865405,
       -47.09890932398194,
       3225.21758291584], dtype='float64');
Covr0=array([[1.215262857583523e-06, 9.619648373341483e-08, -1.621366168297976e-07],
       [9.619648351151952e-08, 2.414747043400696e-06, 1.451138830771309e-07],
       [-1.621366168498906e-07, 1.451138830389375e-07, 4.930022417118734e-08]], dtype='float64');
Covt0=array([[14.8399826718823, -2.771637684818753, -2.947279171506902],
       [-2.77163768705497, 11.23342540647481, 3.82132796844131],
       [-2.947279172002353, 3.821327968136301, 5.732002797523863]], dtype='float64');
r1=array([-0.3729529096726589,
       0.1283567484937524,
       -0.09099573920587016], dtype='float64');
t1=array([-808.543656349386,
       51.72662926454768,
       4341.09166243214], dtype='float64');
Covr1=array([[1.28728712777605e-06, 2.292031019755745e-07, 7.164063336315167e-08],
       [2.292031017899947e-07, 1.517545280677028e-06, 1.908345707894411e-07],
       [7.164063333596253e-08, 1.908345708017118e-07, 4.152510641681152e-08]], dtype='float64');
Covt1=array([[26.43290153753483, -5.340841415121381, -0.5470070590858325],
       [-5.340841419155443, 20.77501553719048, 5.591590318953009],
       [-0.5470070598102738, 5.591590319090976, 8.512032998723376]], dtype='float64');
r2=array([-0.029792141283283,
       -0.01837214815186982,
       -0.135697951901919], dtype='float64');
t2=array([-1093.823307075787,
       -37.86634370109059,
       3449.594503624166], dtype='float64');
Covr2=array([[1.348702897047455e-06, 6.322544232814832e-08, 3.973958737024121e-08],
       [6.322544220400317e-08, 1.418668113116079e-06, -5.113322325280512e-08],
       [3.973958737368252e-08, -5.113322324853446e-08, 8.659484211496633e-09]], dtype='float64');
Covt2=array([[16.94015204692767, -3.467894892072614, 0.7223935721300071],
       [-3.467894894676443, 13.53574072463292, 3.726713588498053],
       [0.7223935716293948, 3.726713588764242, 7.460358963360001]], dtype='float64');
r3=array([-0.2301345710011641,
       -1.140741743578172,
       0.1197783912377829], dtype='float64');
t3=array([-671.399226064902,
       -374.6136342155381,
       452.7219400518998], dtype='float64');
Covr3=array([[9.239854990715772e-07, 2.478930020349381e-07, -4.178734900027066e-07],
       [2.478930018605905e-07, 1.221881699406224e-06, -9.434689066048653e-09],
       [-4.178734900194372e-07, -9.434689159732426e-09, 2.431159992353492e-07]], dtype='float64');
Covt3=array([[0.4581865142589329, -0.120400265711733, 0.005837400572988522],
       [-0.1204002657736983, 0.3603645670460703, 0.4442406623774273],
       [0.005837400504439017, 0.4442406624155747, 1.328467781852049]], dtype='float64');
r4=array([-0.249922916436406,
       -0.8956020702125257,
       0.1101312656752084], dtype='float64');
t4=array([-1307.158771876849,
       -207.3365743334648,
       1414.721245452767], dtype='float64');
Covr4=array([[9.594518863668866e-07, 1.989303502116493e-07, -2.546075859868714e-07],
       [1.989303500478807e-07, 1.218575855545515e-06, -9.708987601389545e-09],
       [-2.546075859954682e-07, -9.708987662077601e-09, 1.239199968175079e-07]], dtype='float64');
Covt4=array([[3.685696556980427, -0.809327140762207, 0.4830089805969682],
       [-0.8093271413055058, 2.973522218032862, 1.52371002469436],
       [0.4830089803395665, 1.523710024903163, 3.991150795010905]], dtype='float64');
r5=array([1.041278224259968,
       -0.06589316894038309,
       -0.0485322003275391], dtype='float64');
t5=array([-1099.079431372368,
       -402.6027782548282,
       3106.893371739462], dtype='float64');
Covr5=array([[1.204120895495361e-06, 2.8014451631075e-07, -1.694305280151591e-07],
       [2.801445161239209e-07, 1.265113750383784e-06, -6.446866454130562e-07],
       [-1.694305279130288e-07, -6.446866454169377e-07, 3.855422826653681e-07]], dtype='float64');
Covt5=array([[13.90973028618363, -2.971438545781883, 1.057938851944193],
       [-2.971438547897332, 10.93671100120915, 3.54347238815986],
       [1.057938851385224, 3.54347238849246, 7.061598270958007]], dtype='float64');
r6=array([0.02555384460701291,
       -0.6052796772539706,
       -1.019549879493904], dtype='float64');
t6=array([-852.4454460896623,
       774.0949447436839,
       2841.191082327033], dtype='float64');
Covr6=array([[9.686046794532616e-07, -6.308503206524856e-08, -1.806080997820153e-07],
       [-6.308503226465711e-08, 1.672316003773063e-06, -2.465547833862028e-07],
       [-1.806080997535351e-07, -2.465547834351338e-07, 9.596772658001584e-08]], dtype='float64');
Covt6=array([[12.05294634257851, -2.389102326022924, 0.4919129660416495],
       [-2.389102327848932, 9.336987961695051, 1.001892009434843],
       [0.4919129659996407, 1.001892009588357, 5.220438607603415]], dtype='float64');
r7=array([-0.8193576101921614,
       0.136124540227304,
       0.08397464312489696], dtype='float64');
t7=array([-520.7199160573418,
       359.6921155124193,
       3742.39686446023], dtype='float64');
Covr7=array([[1.004503557328007e-06, 2.350675616996548e-07, 1.204100212883732e-07],
       [2.350675615142962e-07, 1.254160031629726e-06, 4.135146304957001e-07],
       [1.204100212256213e-07, 4.135146305050297e-07, 1.528740945531735e-07]], dtype='float64');
Covt7=array([[19.7258058180384, -3.878908007396821, -1.035072957041635],
       [-3.878908010408865, 15.40851147689714, 3.462253150662004],
       [-1.035072957450432, 3.462253150642185, 5.430243331660783]], dtype='float64');
r8=array([-0.9885348581720865,
       0.2966577577657575,
       0.4369888002977804], dtype='float64');
t8=array([-564.6578404234365,
       298.0135711886681,
       5049.544430280229], dtype='float64');
Covr8=array([[1.287539953485534e-06, 1.550167574335424e-07, 3.223849761388057e-07],
       [1.550167572399822e-07, 1.291230057590368e-06, 5.194985489883992e-07],
       [3.223849760588663e-07, 5.194985490318159e-07, 3.070494003718257e-07]], dtype='float64');
Covt8=array([[35.65568387522148, -6.947386506647333, -2.3655355737898],
       [-6.947386512112226, 28.25701019248392, 6.384744088340046],
       [-2.365535574568317, 6.384744088223763, 9.275789211895058]], dtype='float64');
r9=array([-0.5440044168516159,
       0.1010986343061286,
       1.380392812136213], dtype='float64');
t9=array([-1466.312267195604,
       -225.1827915560656,
       4992.267998125853], dtype='float64');
Covr9=array([[2.310142239459972e-06, 4.564375206591536e-07, 5.441764253743818e-07],
       [4.564375204602395e-07, 2.33409177414342e-06, -1.105063874591078e-07],
       [5.441764253717119e-07, -1.105063873998112e-07, 2.046777700435373e-07]], dtype='float64');
Covt9=array([[37.45124781929177, -8.411821552336358, -2.863601048006974],
       [-8.411821557909478, 28.63921800556185, 10.10847087978593],
       [-2.863601049495837, 10.10847087984411, 16.67775378146694]], dtype='float64');
r10=array([-0.4199885213593201,
       -0.1558609785865289,
       -0.1584636894128571], dtype='float64');
t10=array([-1116.142984463629,
       687.5874910722442,
       5443.685829961252], dtype='float64');
Covr10=array([[7.517662334760856e-06, -1.468516081215415e-06, 5.109548737225621e-07],
       [-1.468516081384054e-06, 5.263469825484771e-06, -2.09633991804072e-07],
       [5.109548737002982e-07, -2.096339918141228e-07, 1.39749231838419e-07]], dtype='float64');
Covt10=array([[42.56805997803112, -8.90927482378164, -2.279648300051441],
       [-8.909274830274663, 34.47572800185534, 9.966094315249302],
       [-2.279648300836856, 9.966094315323128, 22.65120756599647]], dtype='float64');
r11=array([0.5644970368889765,
       -0.1042917547256826,
       0.02547360068423708], dtype='float64');
t11=array([-1069.30501729995,
       578.8447139406155,
       4513.168649903724], dtype='float64');
Covr11=array([[1.907654650994227e-06, 2.58848466890857e-07, -4.554334812355736e-08],
       [2.588484666904657e-07, 1.695110920638885e-06, -6.375732868337638e-07],
       [-4.554334804578545e-08, -6.375732868373492e-07, 3.040675222937519e-07]], dtype='float64');
Covt11=array([[29.23335160315434, -5.938911368910293, -0.2567435556714585],
       [-5.938911373386272, 23.35269667929798, 5.874231741202475],
       [-0.2567435562646357, 5.874231741433605, 14.22766143218785]], dtype='float64');