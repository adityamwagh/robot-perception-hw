# AprilCalib log 19
# CalibRig::mode=2d
# @ Fri Dec  3 18:20:58 2021

from numpy import array
U=array([[360.5335388183594, 327.5504150390625, 463.0660705566406, 301.6824951171875, 403.8291931152344, 302.5522766113281, 404.9341430664062, 328.6376037597656, 361.6830139160156],
       [294.5675964355469, 289.2860412597656, 312.0376892089844, 284.9976501464844, 302.0887451171875, 358.1685180664062, 409.76513671875, 371.3710632324219, 387.9529418945312]], dtype='float64');
Xw=array([[1099.504516601562, 899.5044555664062, 1499.504516601562, 699.5044555664062, 1299.504516601562, 699.5044555664062, 1299.504516601562, 899.5044555664062, 1099.504516601562],
       [99.50446319580078, 99.50446319580078, 99.50446319580078, 99.50446319580078, 99.50446319580078, 299.5044555664062, 299.5044555664062, 299.5044555664062, 299.5044555664062],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype='float64');
# After LM:
K=array([[638.9939689639434, 0, 330.5911107643521],
       [0, 637.9324319960733, 245.2684848415949],
       [0, 0, 1]], dtype='float64');
distCoeffs=array([-0.05195410258780461,
       0.003661110857187317,
       0.006245294005029294,
       0.0008223104209531926,
       0], dtype='float64');
CovK=array([[0.1329273840824528, 0.1265399241458115, 0.05910278247652978, -0.07132280182344172, 0.0001172502256005502, 0.0005047938142856595, -3.144132059905194e-05, 1.958429374746629e-05, -0.001076895801891561],
       [0.1265399241459348, 0.1307367688763533, 0.0556252173415854, -0.06674288241977301, 0.0001575298643549676, 0.0003644121338380338, -3.789572340656816e-05, 1.708128868565912e-05, -0.0008501197210887021],
       [0.05910278246773693, 0.05562521733258819, 0.4922784907303178, -0.0680435204184336, 5.7095484541326e-05, 0.0009716480582172015, -3.453097835610008e-05, 0.00019719673901276, -0.002360930153563706],
       [-0.0713228018246003, -0.06674288242065632, -0.06804352043887062, 0.3907353274152777, -0.0002678575584301662, 0.0001047651204079922, 0.0001619788812005001, -3.037336726840117e-05, 0.0002484728448529101],
       [0.0001172502256004821, 0.0001575298643547616, 5.709548455974537e-05, -0.0002678575584228591, 7.788858152062983e-06, -4.224063430538381e-05, -3.039590443003762e-07, 3.171611099794115e-08, 7.775943787027586e-05],
       [0.0005047938142725976, 0.0003644121338241924, 0.0009716480581899879, 0.0001047651204058326, -4.224063430539795e-05, 0.0002773263076780922, 7.893105993191885e-07, 3.639832341856561e-07, -0.0005431017129663921],
       [-3.144132059938686e-05, -3.789572340679034e-05, -3.453097836461307e-05, 0.0001619788811999939, -3.039590443025225e-07, 7.893105993155976e-07, 9.185609860472611e-08, -1.526157655009245e-08, -1.230231466071965e-06],
       [1.958429374404062e-05, 1.708128868214389e-05, 0.0001971967390132504, -3.0373367260455e-05, 3.171611099081789e-08, 3.639832341986557e-07, -1.526157654679192e-08, 8.843603979520343e-08, -9.066371435225551e-07],
       [-0.001076895801860156, -0.0008501197210551453, -0.002360930153525234, 0.0002484728448436444, 7.775943787030884e-05, -0.0005431017129664064, -1.230231466085313e-06, -9.066371435009879e-07, 0.001106417604705755]], dtype='float64');
# rms=0.191412
r0=array([-0.382938575984687,
       -0.02237448473654909,
       0.04895228311984502], dtype='float64');
t0=array([204.9026927478332,
       -51.84258637206429,
       3237.222600946974], dtype='float64');
Covr0=array([[1.13587152962445e-06, 1.538662071448604e-08, -1.573387623840584e-07],
       [1.538662066236979e-08, 1.954976545317178e-06, 1.227484814976575e-07],
       [-1.573387623889924e-07, 1.22748481489749e-07, 4.624300724876371e-08]], dtype='float64');
Covt0=array([[12.73283379861658, -1.464783535970885, -1.29048704770859],
       [-1.464783536491239, 9.866713047019381, 2.360794013772045],
       [-1.29048704795657, 2.360794013751366, 3.650662075667628]], dtype='float64');
r1=array([-0.3717168406045429,
       0.125386243648172,
       -0.09123634711991263], dtype='float64');
t1=array([-821.9557434607078,
       45.27886048332635,
       4354.631964957654], dtype='float64');
Covr1=array([[1.20156264170073e-06, 1.238387948054424e-07, 5.236442892323499e-08],
       [1.238387947617807e-07, 1.330022809764051e-06, 1.582358265179394e-07],
       [5.236442891686336e-08, 1.582358265204847e-07, 3.550730508571213e-08]], dtype='float64');
Covt1=array([[22.64963938387745, -2.93903773277921, 1.609050496110708],
       [-2.939037733727262, 18.24926703213671, 3.455752873835337],
       [1.609050495677318, 3.455752873961852, 5.868557647014998]], dtype='float64');
r2=array([-0.02804273807973928,
       -0.01956787104462848,
       -0.1356154040322013], dtype='float64');
t2=array([-1104.650272699262,
       -42.99837826092745,
       3461.772547092264], dtype='float64');
Covr2=array([[1.308535105382531e-06, 2.281761687561946e-08, 4.089534731247908e-08],
       [2.281761684789105e-08, 1.286563679823717e-06, -4.859219068875436e-08],
       [4.089534731333979e-08, -4.859219068778853e-08, 8.636283774312511e-09]], dtype='float64');
Covt2=array([[14.51270292706227, -1.913065425127256, 2.05123764878444],
       [-1.913065425739969, 11.89223570465298, 2.301198619506359],
       [2.051237648490704, 2.301198619622787, 5.505093113977707]], dtype='float64');
r3=array([-0.2283394543332531,
       -1.143168543234247,
       0.1188216283570481], dtype='float64');
t3=array([-673.3794420422053,
       -375.0494169570201,
       455.8055961454885], dtype='float64');
Covr3=array([[8.109964942234199e-07, 1.569749947251416e-07, -3.714037746092579e-07],
       [1.569749946862094e-07, 1.075803567376153e-06, 2.309215271665581e-08],
       [-3.714037746136167e-07, 2.309215269553967e-08, 2.230769140351207e-07]], dtype='float64');
Covt3=array([[0.3831623272214191, -0.06970539103381458, 0.1100260996461522],
       [-0.069705391048781, 0.3145179037188395, 0.3397877136432177],
       [0.1100260996177017, 0.3397877136568694, 1.037211972090601]], dtype='float64');
r4=array([-0.2479923521720737,
       -0.8977672653569759,
       0.1093718151833316], dtype='float64');
t4=array([-1312.47254087399,
       -209.2838070926342,
       1421.170332407511], dtype='float64');
Covr4=array([[8.405619472406483e-07, 1.138223621084421e-07, -2.262730617738571e-07],
       [1.138223620708363e-07, 1.079890554574605e-06, 8.285107482432694e-09],
       [-2.262730617755487e-07, 8.285107468749944e-09, 1.165453486176709e-07]], dtype='float64');
Covt4=array([[3.12639979934382, -0.4381645648027844, 0.9215695549015073],
       [-0.4381645649313263, 2.607913073011332, 1.05966921478136],
       [0.921569554784092, 1.059669214852577, 3.155927737351846]], dtype='float64');
r5=array([1.042786163662643,
       -0.06862413887560037,
       -0.04705057737986019], dtype='float64');
t5=array([-1108.848505794492,
       -406.964430726002,
       3117.036423218945], dtype='float64');
Covr5=array([[1.055037316917104e-06, 1.618937420500804e-07, -9.902605532286006e-08],
       [1.618937420059099e-07, 1.094453264321815e-06, -5.467776882114653e-07],
       [-9.902605529867502e-08, -5.467776882126914e-07, 3.292174526704821e-07]], dtype='float64');
Covt5=array([[11.92150092522653, -1.688736450228634, 2.210999595440946],
       [-1.688736450724205, 9.612509157666139, 2.287253018538551],
       [2.210999595147741, 2.287253018678729, 5.391072633535923]], dtype='float64');
r6=array([0.02797083287710396,
       -0.6069074181486239,
       -1.020074879104948], dtype='float64');
t6=array([-861.7684886013514,
       769.9582968858501,
       2853.880049655563], dtype='float64');
Covr6=array([[9.270425194784156e-07, -9.53836338949125e-08, -1.662267308131056e-07],
       [-9.538363394229587e-08, 1.390852661573391e-06, -1.996340866683498e-07],
       [-1.662267308058995e-07, -1.996340866806109e-07, 8.596896545604249e-08]], dtype='float64');
Covt6=array([[10.32755258526475, -1.296514102023014, 1.421286660234127],
       [-1.296514102448313, 8.210936754840382, 0.102287050716016],
       [1.421286660088668, 0.1022870508094206, 3.904610229443597]], dtype='float64');
r7=array([-0.8177177558596468,
       0.1329415597843618,
       0.08305327655958485], dtype='float64');
t7=array([-532.4049668133231,
       353.8288236976383,
       3753.987535709065], dtype='float64');
Covr7=array([[9.073571343690687e-07, 1.319571927912665e-07, 8.235697812642308e-08],
       [1.319571927509044e-07, 1.075794720766851e-06, 3.472418512906087e-07],
       [8.235697811292602e-08, 3.472418512928492e-07, 1.279408198422064e-07]], dtype='float64');
Covt7=array([[16.87866684971425, -2.110064633558441, 0.5663816730108587],
       [-2.110064634259479, 13.56803671035417, 1.982157089363271],
       [0.5663816727372858, 1.982157089421651, 3.692992208181016]], dtype='float64');
r8=array([-0.9870357396475664,
       0.2931774364067023,
       0.4359797597593154], dtype='float64');
t8=array([-580.2583511173275,
       289.7349688714739,
       5064.263323073104], dtype='float64');
Covr8=array([[1.157008447722419e-06, 5.560426990419932e-08, 2.537405529917069e-07],
       [5.560426986182453e-08, 1.158774434734322e-06, 4.417582682108326e-07],
       [2.537405529743331e-07, 4.417582682206558e-07, 2.591746463167372e-07]], dtype='float64');
Covt8=array([[30.52721548292709, -3.803472279893374, 0.4222614874103919],
       [-3.803472281161358, 24.98630446435569, 3.819059202573177],
       [0.4222614869198077, 3.819059202648765, 6.271332577549629]], dtype='float64');
r9=array([-0.5439753618940034,
       0.100412868496684,
       1.379923296353498], dtype='float64');
t9=array([-1481.049283726541,
       -232.3677433938867,
       5008.921828016036], dtype='float64');
Covr9=array([[2.178177481210456e-06, 3.872291302833113e-07, 5.259093267590603e-07],
       [3.872291302263401e-07, 2.172336585439056e-06, -1.133004720728029e-07],
       [5.259093267601353e-07, -1.133004720545847e-07, 2.003139542659178e-07]], dtype='float64');
Covt9=array([[31.76901892227212, -4.938580404646557, 1.274183690692653],
       [-4.938580405954797, 25.13973345582721, 6.361998602925243],
       [1.274183690022974, 6.361998603074597, 11.53810492253372]], dtype='float64');
r10=array([-0.4188356121145219,
       -0.1584898081266193,
       -0.1588812807351006], dtype='float64');
t10=array([-1133.17541947602,
       679.3161845687737,
       5463.205312330249], dtype='float64');
Covr10=array([[7.36303449802831e-06, -1.541140906196859e-06, 5.052644247850681e-07],
       [-1.541140906238612e-06, 5.087724696756351e-06, -2.181989007223485e-07],
       [5.052644247804244e-07, -2.181989007241867e-07, 1.371676057247326e-07]], dtype='float64');
Covt10=array([[36.4754225031906, -5.026703445118516, 1.338128897674609],
       [-5.026703446635175, 30.38541669760663, 6.457346598959925],
       [1.338128897070108, 6.457346599135012, 18.01545799339626]], dtype='float64');
r11=array([0.5672107669164285,
       -0.1066109866444124,
       0.02643010912644622], dtype='float64');
t11=array([-1083.591107503823,
       572.1687448800989,
       4530.122450082946], dtype='float64');
Covr11=array([[1.805426438328852e-06, 1.763192014254462e-07, -8.89742428968363e-09],
       [1.763192013816546e-07, 1.521497060323053e-06, -5.688145169678731e-07],
       [-8.897424272591365e-09, -5.688145169684091e-07, 2.767769590774616e-07]], dtype='float64');
Covt11=array([[25.04941271628707, -3.246858942088439, 2.198829947189014],
       [-3.246858943145945, 20.4950828497788, 3.297869881918975],
       [2.198829946700442, 3.297869882077089, 10.60000344220816]], dtype='float64');
r12=array([-0.3718541452126247,
       -0.9694869929339305,
       -0.1209934344960301], dtype='float64');
t12=array([-1320.196899425794,
       -33.20153819937753,
       720.7118640653601], dtype='float64');
Covr12=array([[1.042248136119218e-06, 6.751965576351924e-08, -2.362978991300026e-07],
       [6.751965570776131e-08, 1.353616811722695e-06, 6.769745183542542e-08],
       [-2.362978991324109e-07, 6.769745181653262e-08, 1.747506556897996e-07]], dtype='float64');
Covt12=array([[1.465142579405712, -0.2437155217482703, 0.1622985924700517],
       [-0.2437155217779281, 1.042904575917116, 0.5470678211779046],
       [0.1622985923541953, 0.5470678212468727, 2.904102608338012]], dtype='float64');
r13=array([-0.3572627332884844,
       0.9819379290063013,
       -0.03357619859845349], dtype='float64');
t13=array([601.8333893648236,
       230.7315759559252,
       3183.12734158428], dtype='float64');
Covr13=array([[1.38222749529453e-06, 1.659988627461257e-07, 1.040255333153837e-07],
       [1.659988627096913e-07, 1.550633343814538e-06, 1.518119748695425e-08],
       [1.04025533313672e-07, 1.518119750150554e-08, 3.002302484450897e-07]], dtype='float64');
Covt13=array([[12.35326304521788, -1.572022259183631, -2.525820985972874],
       [-1.572022259690572, 10.10461409923933, 2.487685581698224],
       [-2.525820986179583, 2.487685581611723, 5.12203155897201]], dtype='float64');
r14=array([-0.8518815925980746,
       0.7612857332088627,
       1.163094576867336], dtype='float64');
t14=array([837.3644838496502,
       898.0667130587127,
       4196.2460521336], dtype='float64');
Covr14=array([[1.434734944606938e-06, 1.945083521088123e-07, 5.188143177338389e-07],
       [1.945083520662681e-07, 1.504729431839759e-06, 2.25798283755791e-07],
       [5.188143177258292e-07, 2.257982837739898e-07, 3.11156322218667e-07]], dtype='float64');
Covt14=array([[21.70957695727665, -3.359462559023791, -6.190770804798851],
       [-3.359462559927275, 17.97179189108067, 2.745421441171159],
       [-6.190770805106581, 2.745421440955392, 7.737496360443042]], dtype='float64');
r15=array([-1.104993234109014,
       0.4654149660483106,
       0.514350851844999], dtype='float64');
t15=array([1605.916423536856,
       629.5363382251894,
       4010.865908295353], dtype='float64');
Covr15=array([[1.364266402837018e-06, 1.085251700253311e-07, 2.463497123061201e-07],
       [1.08525169986986e-07, 2.104342600718591e-06, 9.804520836641163e-08],
       [2.463497122859006e-07, 9.804520836911932e-08, 6.627240166964752e-07]], dtype='float64');
Covt15=array([[20.6824565819967, -2.61487949569496, -7.115657502075106],
       [-2.61487949653485, 17.79677697048305, 6.198211824679761],
       [-7.11565750246213, 6.1982118242731, 20.0980855560345]], dtype='float64');
r16=array([-0.5814917315079736,
       0.8226199759402164,
       0.4734113257802178], dtype='float64');
t16=array([959.8731325394275,
       129.4830060693565,
       2858.221284924198], dtype='float64');
Covr16=array([[1.439295929061668e-06, -8.63863424904883e-08, 3.121832866399268e-07],
       [-8.638634252470947e-08, 1.813129597591457e-06, 1.398195126178417e-07],
       [3.121832866308929e-07, 1.398195126296964e-07, 2.557178138190534e-07]], dtype='float64');
Covt16=array([[10.12860601340743, -1.291094032098347, -3.897648807296314],
       [-1.291094032524028, 8.506530371884526, 2.666158480923194],
       [-3.897648807513792, 2.666158480786441, 4.964901967661016]], dtype='float64');
r17=array([0.04190635338709055,
       1.43697538155964,
       0.08082252446585877], dtype='float64');
t17=array([749.4133349004761,
       -120.9404704191788,
       2142.211780549234], dtype='float64');
Covr17=array([[1.110091785792086e-06, 2.316209587862003e-07, 4.994358106323717e-07],
       [2.316209587486825e-07, 1.37499845873483e-06, -1.402492885475277e-08],
       [4.994358106381993e-07, -1.402492883087211e-08, 3.533171336614721e-07]], dtype='float64');
Covt17=array([[5.91105184639724, -0.7489882530242425, -1.95134270845324],
       [-0.748988253269783, 4.76186639185027, 1.715040173658399],
       [-1.951342708592546, 1.715040173592147, 2.934012614659776]], dtype='float64');
r18=array([0.01140625732368186,
       1.382522454467851,
       -0.002539579645577886], dtype='float64');
t18=array([489.8949424362341,
       -75.58663473026766,
       2352.968788698446], dtype='float64');
Covr18=array([[8.07952652925208e-07, 2.033724881210724e-07, 4.02332347628272e-07],
       [2.033724880835927e-07, 1.15256256920399e-06, -6.171493692062303e-09],
       [4.023323476332637e-07, -6.171493668162797e-09, 2.91806677791368e-07]], dtype='float64');
Covt18=array([[6.791061898444872, -0.8794812121962444, -1.57286547829496],
       [-0.8794812124720478, 5.353978959637913, 1.34968214827846],
       [-1.572865478414617, 1.349682148231927, 1.757018037052563]], dtype='float64');
r19=array([0.006053541641175155,
       1.205023675666669,
       -0.01098647490035697], dtype='float64');
t19=array([-330.186968864841,
       12.66653547403183,
       2399.010010649268], dtype='float64');
Covr19=array([[8.754572649269442e-07, 2.076979329509724e-07, 3.929996628145055e-07],
       [2.076979329056381e-07, 1.226475785704541e-06, 5.17514560019154e-09],
       [3.929996628187448e-07, 5.175145625708113e-09, 3.451626559674218e-07]], dtype='float64');
Covt19=array([[6.872941631564085, -0.8441876943475238, 0.5408947520484952],
       [-0.8441876946270129, 5.370248168591875, 0.5671086242153438],
       [0.5408947519748848, 0.5671086242452072, 0.7416417135130311]], dtype='float64');
