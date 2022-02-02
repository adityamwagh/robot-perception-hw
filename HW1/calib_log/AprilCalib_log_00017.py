# AprilCalib log 17
# CalibRig::mode=2d
# @ Fri Dec  3 18:20:55 2021

from numpy import array
U=array([[565.7621459960938, 599.3966064453125, 562.163330078125, 594.9772338867188, 558.6016235351562, 590.67431640625, 555.1148681640625, 586.7357788085938],
       [241.5703430175781, 246.7325286865234, 302.6824035644531, 314.5032958984375, 363.3276672363281, 380.7640380859375, 422.5652770996094, 445.9835510253906]], dtype='float64');
Xw=array([[99.50446319580078, 299.5044555664062, 99.50446319580078, 299.5044555664062, 99.50446319580078, 299.5044555664062, 99.50446319580078, 299.5044555664062],
       [99.50446319580078, 99.50446319580078, 299.5044555664062, 299.5044555664062, 499.5044555664062, 499.5044555664062, 699.5044555664062, 699.5044555664062],
       [0, 0, 0, 0, 0, 0, 0, 0]], dtype='float64');
# After LM:
K=array([[638.2119861706002, 0, 329.6052340667956],
       [0, 636.9012390932995, 244.4690012761282],
       [0, 0, 1]], dtype='float64');
distCoeffs=array([-0.05844221724180856,
       0.02085984769226294,
       0.006443874046211984,
       0.0005528127737108021,
       0], dtype='float64');
CovK=array([[0.1943630434139585, 0.1877574227846492, 0.1010326500176683, -0.1167020027787919, 0.0001850239239537557, 0.0006700205694758967, -4.661189460496048e-05, 3.159919663471113e-05, -0.001586075200272709],
       [0.1877574227848234, 0.191916638757003, 0.09902519657285531, -0.1117113509818455, 0.0002275740253783436, 0.0005267535769696664, -5.344207988762904e-05, 2.967788743798848e-05, -0.001370776571717265],
       [0.1010326500261109, 0.09902519657987008, 0.5317080627170417, -0.1027998600198851, 9.68441385377243e-05, 0.001221758635539259, -4.747262588389169e-05, 0.0002101111141547535, -0.003013685519602804],
       [-0.1167020027753793, -0.1117113509783282, -0.1027998600052362, 0.431034968327242, -0.0003309266930783894, 5.433156883848613e-05, 0.000175404612310926, -4.139367376140975e-05, 0.0005074390310332971],
       [0.0001850239239507347, 0.000227574025375283, 9.684413850824565e-05, -0.0003309266930822874, 8.104935469639428e-06, -4.358130624722273e-05, -3.331238511916032e-07, 4.097999152283644e-08, 8.015424760440657e-05],
       [0.0006700205694868928, 0.0005267535769769758, 0.001221758635560085, 5.433156882294539e-05, -4.358130624719437e-05, 0.0002889699934733628, 8.026729073394783e-07, 4.569921485681904e-07, -0.0005682993660056097],
       [-4.661189460344614e-05, -5.344207988606342e-05, -4.747262587703609e-05, 0.0001754046123109407, -3.331238511903387e-07, 8.026729073495139e-07, 9.743776341054644e-08, -1.94220979449059e-08, -1.188031705836623e-06],
       [3.159919663844588e-05, 2.967788744114294e-05, 0.0002101111141560873, -4.139367376744825e-05, 4.097999153291293e-08, 4.569921485789315e-07, -1.942209794772415e-08, 9.281918244643422e-08, -1.128203384336236e-06],
       [-0.001586075200286047, -0.001370776571721527, -0.003013685519598533, 0.0005074390310687958, 8.015424760435307e-05, -0.0005682993660055086, -1.188031705814703e-06, -1.12820338429342e-06, 0.001165506418428553]], dtype='float64');
# rms=0.186384
r0=array([-0.38333218940793,
       -0.02010516626567618,
       0.04922297948584345], dtype='float64');
t0=array([210.0271597993179,
       -47.75640550582024,
       3233.242038410786], dtype='float64');
Covr0=array([[1.187011314173502e-06, 1.07268439488727e-07, -1.562894847376562e-07],
       [1.072684395215723e-07, 2.161454210218164e-06, 1.283265132875404e-07],
       [-1.562894847347444e-07, 1.283265132939439e-07, 4.691411106320162e-08]], dtype='float64');
Covt0=array([[13.74921677282373, -2.334964129867171, -2.434347369022904],
       [-2.334964129491437, 10.88134531458983, 3.536227612583453],
       [-2.43434736881091, 3.536227612675127, 5.292097140340935]], dtype='float64');
r1=array([-0.3725493392951257,
       0.1270125442168777,
       -0.09116731456457546], dtype='float64');
t1=array([-815.3035106968473,
       50.86153208751737,
       4350.457454312071], dtype='float64');
Covr1=array([[1.263144843666275e-06, 1.947082943762322e-07, 6.584785288015953e-08],
       [1.947082943966984e-07, 1.424164331222549e-06, 1.745764859772233e-07],
       [6.584785288300068e-08, 1.745764859744158e-07, 3.864336630289636e-08]], dtype='float64');
Covt1=array([[24.46983151507205, -4.518584910329857, -0.03359377457533053],
       [-4.518584909647416, 20.10561083552243, 5.243767451884851],
       [-0.03359377416362531, 5.243767451931356, 8.037293319958989]], dtype='float64');
r2=array([-0.0291158809338282,
       -0.01929754690379649,
       -0.1356486190465961], dtype='float64');
t2=array([-1099.267583013684,
       -38.55521751025933,
       3457.379802629845], dtype='float64');
Covr2=array([[1.335958464078482e-06, 3.727250183256534e-08, 4.072955966381803e-08],
       [3.727250185527412e-08, 1.345170265679757e-06, -5.030730058716095e-08],
       [4.072955966334916e-08, -5.030730058835561e-08, 8.694085023453991e-09]], dtype='float64');
Covt2=array([[15.68147977408097, -2.939729109370775, 0.9957546596696252],
       [-2.939729108924023, 13.10496817974347, 3.536771995159977],
       [0.9957546599896092, 3.536771995156224, 7.129913696980674]], dtype='float64');
r3=array([-0.2298579168893123,
       -1.141883130821362,
       0.1194818072462845], dtype='float64');
t3=array([-672.4854356862028,
       -374.5863626830266,
       455.0075347049612], dtype='float64');
Covr3=array([[8.888611666656984e-07, 2.136176981267456e-07, -4.040401668349214e-07],
       [2.136176981536432e-07, 1.134722545574771e-06, 1.973758061954216e-09],
       [-4.040401668323002e-07, 1.97375807667135e-09, 2.371830689383383e-07]], dtype='float64');
Covt3=array([[0.4274527957094572, -0.1050764135773947, 0.02206142589700462],
       [-0.1050764135664366, 0.3499392987366489, 0.4284784959331049],
       [0.02206142591738254, 0.4284784959283627, 1.279269102652788]], dtype='float64');
r4=array([-0.2497402131686728,
       -0.8965250634573499,
       0.1098443798349445], dtype='float64');
t4=array([-1310.066079022791,
       -207.5125120752032,
       1419.495183585423], dtype='float64');
Covr4=array([[9.241986995886641e-07, 1.687525361332741e-07, -2.459517937274978e-07],
       [1.687525361579236e-07, 1.133623977402819e-06, -2.219545535694291e-09],
       [-2.459517937258486e-07, -2.219545526195891e-09, 1.213143654136764e-07]], dtype='float64');
Covt4=array([[3.431263654105906, -0.6925273327771583, 0.5355269294390104],
       [-0.6925273326811804, 2.884094444761642, 1.465200012506301],
       [0.5355269295452293, 1.465200012483425, 3.844952438927808]], dtype='float64');
r5=array([1.041260280118554,
       -0.0673210973161131,
       -0.04776018177909239], dtype='float64');
t5=array([-1104.002032713277,
       -403.2356919127052,
       3113.997889829225], dtype='float64');
Covr5=array([[1.163297462872797e-06, 2.421712047693387e-07, -1.458129658854819e-07],
       [2.42171204803013e-07, 1.175686516057533e-06, -5.942001762869942e-07],
       [-1.458129659040677e-07, -5.942001762872263e-07, 3.569153517437014e-07]], dtype='float64');
Covt5=array([[12.88142120976544, -2.527937133848062, 1.284791835893234],
       [-2.527937133492946, 10.59116855558161, 3.347729118513473],
       [1.284791836160907, 3.347729118491544, 6.768403405960901]], dtype='float64');
r6=array([0.02655471394080662,
       -0.6064584422232804,
       -1.019640380526508], dtype='float64');
t6=array([-857.0679590421671,
       773.6070848988558,
       2848.907010676646], dtype='float64');
Covr6=array([[9.478879110924795e-07, -5.271443059516937e-08, -1.77487757914524e-07],
       [-5.271443056430873e-08, 1.545194410835804e-06, -2.304858756027827e-07],
       [-1.774877579194053e-07, -2.304858755934311e-07, 9.294664193781315e-08]], dtype='float64');
Covt6=array([[11.16818977847091, -2.019543430575943, 0.657669111973362],
       [-2.019543430269363, 9.04668619001612, 0.8988987568969015],
       [0.6576691120977753, 0.8988987569015872, 4.967134424986594]], dtype='float64');
r7=array([-0.8188553403068815,
       0.1346006047755902,
       0.08346985101149287], dtype='float64');
t7=array([-526.6191031613799,
       358.8091736371043,
       3750.277110026508], dtype='float64');
Covr7=array([[9.765630603407878e-07, 2.017215197147421e-07, 1.076191009962147e-07],
       [2.017215197398022e-07, 1.164218823589354e-06, 3.796967618183618e-07],
       [1.076191010048305e-07, 3.796967618173058e-07, 1.399735906553693e-07]], dtype='float64');
Covt7=array([[18.2487976771007, -3.270472450876774, -0.6063874470959582],
       [-3.270472450368994, 14.90973940238695, 3.197140248595403],
       [-0.6063874468253556, 3.19714024863838, 5.085239530859651]], dtype='float64');
r8=array([-0.9881027757627587,
       0.2949820225931308,
       0.4364118847955679], dtype='float64');
t8=array([-572.5663720922543,
       296.5467772491266,
       5059.586561428405], dtype='float64');
Covr8=array([[1.241865166744503e-06, 1.146567420643474e-07, 2.952705104622202e-07],
       [1.146567420907349e-07, 1.216551880935006e-06, 4.785039301170825e-07],
       [2.952705104733832e-07, 4.785039301116745e-07, 2.833545585206369e-07]], dtype='float64');
Covt8=array([[32.99485692332831, -5.867462507360474, -1.629312740002235],
       [-5.867462506446769, 27.36089973230511, 5.942415018477491],
       [-1.629312739514575, 5.942415018562976, 8.709350058850934]], dtype='float64');
r9=array([-0.5442338067824838,
       0.09906597834618736,
       1.380522556581566], dtype='float64');
t9=array([-1474.44006705365,
       -226.2336759477031,
       5004.612971868138], dtype='float64');
Covr9=array([[2.24019706919134e-06, 4.203365898888284e-07, 5.283864888832168e-07],
       [4.203365898931977e-07, 2.260671672807163e-06, -1.121644464574165e-07],
       [5.283864888832072e-07, -1.12164446457662e-07, 1.989338759948035e-07]], dtype='float64');
Covt9=array([[34.6393362994642, -7.217939130755681, -1.810999472998529],
       [-7.217939129831477, 27.72421498750035, 9.458966984104521],
       [-1.810999472236462, 9.458966984168795, 15.73726388243632]], dtype='float64');
r10=array([-0.4195740552747145,
       -0.1572853883720844,
       -0.1586569188924548], dtype='float64');
t10=array([-1124.744614220422,
       686.4765399505211,
       5456.473752011746], dtype='float64');
Covr10=array([[7.467442261261065e-06, -1.483586122828043e-06, 5.108829380065704e-07],
       [-1.483586122809482e-06, 5.178971309458894e-06, -2.173958680401043e-07],
       [5.108829380078969e-07, -2.173958680363818e-07, 1.386273213052936e-07]], dtype='float64');
Covt10=array([[39.41665409283557, -7.587331464759646, -1.42679670750546],
       [-7.5873314636594, 33.3908764324601, 9.416288876384028],
       [-1.426796706904353, 9.416288876465865, 21.78442141871593]], dtype='float64');
r11=array([0.5653014795333779,
       -0.1055910955132433,
       0.02599201054259962], dtype='float64');
t11=array([-1076.491899494961,
       578.0678534671528,
       4524.452841054785], dtype='float64');
Covr11=array([[1.873012870305186e-06, 2.230913953502801e-07, -3.050451457992112e-08],
       [2.230913953879559e-07, 1.598055165412658e-06, -6.001361477737721e-07],
       [-3.050451459450649e-08, -6.001361477730859e-07, 2.896570254061551e-07]], dtype='float64');
Covt11=array([[27.07965077912406, -5.036142726779101, 0.2656534163865256],
       [-5.036142726003051, 22.61586922340106, 5.511381284375396],
       [0.2656534169093975, 5.511381284419695, 13.59229497627532]], dtype='float64');
r12=array([-0.3735693847468258,
       -0.9684337116795639,
       -0.1203709927836578], dtype='float64');
t12=array([-1318.651500852179,
       -32.31491106794712,
       719.2698513391043], dtype='float64');
Covr12=array([[1.110724913439271e-06, 1.239152714924458e-07, -2.535650054370043e-07],
       [1.239152714972099e-07, 1.425169072455203e-06, 5.735933346946055e-08],
       [-2.53565005434895e-07, 5.735933348488245e-08, 1.796211841548145e-07]], dtype='float64');
Covt12=array([[1.570038169163035, -0.3362176080999005, 0.003991174096007277],
       [-0.3362176080689664, 1.141586638359618, 0.7182349956697768],
       [0.003991173997047171, 0.718234995676462, 3.264994494635761]], dtype='float64');
r13=array([-0.3591142279623032,
       0.9838259608350466,
       -0.0340464626892945], dtype='float64');
t13=array([607.0376177864856,
       235.1223918919592,
       3178.991820036055], dtype='float64');
Covr13=array([[1.451174917587672e-06, 2.462922563813584e-07, 1.288297944367852e-07],
       [2.462922564155714e-07, 1.703635595350698e-06, 4.78420747057324e-08],
       [1.288297944366128e-07, 4.784207469443405e-08, 3.108296994668508e-07]], dtype='float64');
Covt13=array([[13.36178635240857, -2.420941710396258, -3.682269895577361],
       [-2.420941710010598, 11.12644127044166, 3.678816731448286],
       [-3.682269895349349, 3.678816731545778, 6.76636517804423]], dtype='float64');
r14=array([-0.8521498110795247,
       0.7637258394786596,
       1.163331268961434], dtype='float64');
t14=array([843.9448685161792,
       903.6391410512917,
       4189.250314202457], dtype='float64');
Covr14=array([[1.56999544862695e-06, 2.431030037161312e-07, 5.854424631357233e-07],
       [2.431030037467575e-07, 1.542213077741087e-06, 2.523335073525867e-07],
       [5.854424631417677e-07, 2.523335073393633e-07, 3.453729168038761e-07]], dtype='float64');
Covt14=array([[23.45560270796528, -4.911566170793973, -8.294047169891995],
       [-4.911566170128082, 19.81884488961164, 4.874714653667422],
       [-8.294047169579219, 4.87471465394348, 10.73285568303591]], dtype='float64');
r15=array([-1.105492008879541,
       0.4689475382098429,
       0.5148319780223009], dtype='float64');
t15=array([1614.034787615813,
       635.3754610142558,
       4006.53851847768], dtype='float64');
Covr15=array([[1.46485063446851e-06, 2.250018664859192e-07, 3.102800730765813e-07],
       [2.25001866511078e-07, 2.292152212691188e-06, 1.76265769193698e-07],
       [3.102800730915802e-07, 1.762657691921293e-07, 7.047163633235352e-07]], dtype='float64');
Covt15=array([[22.65889590446983, -4.060412270238149, -9.280217091424586],
       [-4.060412269607092, 19.6333303666994, 8.672137475838902],
       [-9.280217091010112, 8.672137476241188, 23.8481265865897]], dtype='float64');
r16=array([-0.5830904138201177,
       0.8262463870574799,
       0.4733134412019124], dtype='float64');
t16=array([964.5976948646535,
       133.358534279909,
       2852.960289192553], dtype='float64');
Covr16=array([[1.509150367580994e-06, -1.353610834154967e-08, 3.519218488222048e-07],
       [-1.353610831815876e-08, 1.960630705393662e-06, 1.896379571868191e-07],
       [3.519218488279314e-07, 1.896379571762509e-07, 2.797374088371311e-07]], dtype='float64');
Covt16=array([[10.94929416487287, -2.001261612929015, -5.053169434064813],
       [-2.001261612619659, 9.364327332054467, 3.835432166155246],
       [-5.053169433869484, 3.835432166312121, 6.829155819910407]], dtype='float64');
r17=array([0.04016489595835108,
       1.439247716314072,
       0.08018207120871933], dtype='float64');
t17=array([753.2212457988541,
       -118.2166785596874,
       2138.832470366787], dtype='float64');
Covr17=array([[1.1917093046493e-06, 3.279930632802065e-07, 5.319209605312051e-07],
       [3.279930633097947e-07, 1.54750795674933e-06, 2.478796283159807e-08],
       [5.319209605262692e-07, 2.478796281325841e-08, 3.669994284479714e-07]], dtype='float64');
Covt17=array([[6.387872836391885, -1.153403842162406, -2.616185011649343],
       [-1.153403841984964, 5.254014420781971, 2.417910004298069],
       [-2.616185011532828, 2.417910004380204, 4.076304547850446]], dtype='float64');