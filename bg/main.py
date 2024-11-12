import requests
import json
import time
import random
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print('Start Parking.py')
# Firebase Realtime Database URL and API key


# Coordinates data
demo = [[37.54489139, 126.89289421],
 [37.53796609, 126.90331806],
 [37.5388433, 126.90146242],
 [37.529664, 126.924537],
 [37.53240356, 126.924436],
 [37.528797, 126.931198],
 [37.52607331, 126.92831446],
 [37.52497241, 126.92532318],
 [37.524501, 126.923781],
 [37.526097, 126.913163],
 [37.52824898, 126.90779447],
 [37.52782182, 126.90463093],
 [37.52625065, 126.89945376],
 [37.526684, 126.902742],
 [37.525797, 126.902025],
 [37.52552609, 126.89579413],
 [37.528464, 126.89437002],
 [37.52579977, 126.88797228],
 [37.52217837, 126.93973139],
 [37.52407584, 126.92604709],
 [37.5240936, 126.9298043],
 [37.52169298376825, 126.92284405231476],
 [37.52432737, 126.89548892],
 [37.51696501, 126.93576386],
 [37.519058, 126.927645],
 [37.51775234, 126.91460391],
 [37.51597645, 126.90749608],
 [37.516095, 126.899927],
 [37.51947074, 126.90260898],
 [37.517985, 126.902785],
 [37.518244, 126.895921],
 [37.51631443, 126.8877957],
 [37.51332538, 126.91407775],
 [37.50834696, 126.89679637],
 [37.50563, 126.910559],
 [37.49965667, 126.89483844],
 [37.49314103, 126.90163365]]
# demo = [
#   [37.68972069, 127.04483862],
#   [37.6876442, 127.04066026],
#   [37.676229, 127.047725],
#   [37.67070279, 127.08041836],
#   [37.6687158, 127.04711546],
#   [37.666646, 127.039654],
#   [37.665784, 127.043741],
#   [37.66482, 127.043719],
#   [37.663147, 127.036928],
#   [37.655348, 127.061802],
#   [37.654954, 127.06086],
#   [37.654867, 127.037972],
#   [37.65671789, 127.01163698],
#   [37.657457, 127.01391],
#   [37.65445795, 127.06369619],
#   [37.65439, 127.049764],
#   [37.65237042, 127.04567683],
#   [37.648654, 127.063009],
#   [37.64775334, 127.03373409],
#   [37.641981, 127.077432],
#   [37.64129794, 127.06801938],
#   [37.64160736, 127.01498164],
#   [37.639866, 127.068575],
#   [37.63709333, 127.03300942],
#   [37.64005648, 127.02595849],
#   [37.636932, 127.023307],
#   [37.63642, 127.070002],
#   [37.63608367, 127.01844991],
#   [37.628515, 127.071146],
#   [37.63091732, 127.06104087],
#   [37.6285679, 127.02235964],
#   [37.631703, 127.02348],
#   [37.62777652, 127.02513238],
#   [37.63061186, 127.01743071],
#   [37.62745359, 127.06201533],
#   [37.62509512, 127.03343189],
#   [37.62400561, 127.01953853],
#   [37.62561503, 127.01770989],
#   [37.62617605, 127.01344244],
#   [37.620514, 127.044938],
#   [37.6221541, 127.03114725],
#   [37.62016376, 127.02031635],
#   [37.62274538, 127.01842794],
#   [37.615743, 127.093825],
#   [37.615292, 127.062997],
#   [37.618662, 127.028891],
#   [37.61695866, 127.0279473],
#   [37.61458475, 127.0251644],
#   [37.612879, 127.099193],
#   [37.61165492, 127.03363616],
#   [37.61417653, 127.03055539],
#   [37.61086046, 127.02974197],
#   [37.60933538, 127.02949836],
#   [37.606535, 127.030397],
#   [37.606548, 127.029027],
#   [37.60838767, 127.02877104],
#   [37.60736694, 127.01009949],
#   [37.601777, 127.096903],
#   [37.601636, 127.040355],
#   [37.600071, 127.104311],
#   [37.599122, 127.098381],
#   [37.59643854, 127.09351851],
#   [37.59178, 127.066602],
#   [37.594584, 126.993775],
#   [37.59098817, 127.06438783],
#   [37.59164441, 127.01442238],
#   [37.583909, 127.086374],
#   [37.58151728, 127.07070593],
#   [37.581328, 127.049055],
#   [37.578574, 127.03242],
#   [37.5782752, 127.07061896],
#   [37.575415, 127.0386],
#   [37.574439, 127.038774],
#   [37.577858, 127.033597],
#   [37.577816, 127.037717],
#   [37.576526, 127.001474],
#   [37.56993873, 127.08469308],
#   [37.56941, 127.066994],
#   [37.56987, 127.04394],
#   [37.56939, 127.04483],
#   [37.5704876, 127.03832741],
#   [37.571538, 127.039926],
#   [37.5696, 127.03263],
#   [37.5707, 127.03429],
#   [37.571558107, 127.03643021],
#   [37.57117, 127.03504624],
#   [37.56944669, 127.0360172],
#   [37.56993875, 127.03514519],
#   [37.5703894, 127.02698474],
#   [37.57063582, 127.02824815],
#   [37.57252061, 127.02425684],
#   [37.57217485, 127.02225792],
#   [37.57002852, 127.01735719],
#   [37.56958258, 127.01316308],
#   [37.56999731, 127.0152055],
#   [37.569577, 127.011183],
#   [37.56960075, 127.01521402],
#   [37.57288249, 127.00816125],
#   [37.56951246, 127.00750172],
#   [37.56948283, 127.00601836],
#   [37.56988704, 127.00756704],
#   [37.56958981, 127.00904766],
#   [37.570031, 127.001665],
#   [37.56934864, 127.00128399],
#   [37.56967214, 127.00112596],
#   [37.57028463, 127.0021223],
#   [37.5730121, 126.99677676],
#   [37.572882, 126.998496],
#   [37.57150398, 126.99496888],
#   [37.57045874, 126.99733225],
#   [37.57278965, 126.99718284],
#   [37.57134087, 126.98776281],
#   [37.565628, 127.173818],
#   [37.565988, 127.172313],
#   [37.566055, 127.160332],
#   [37.5664681574946, 127.16002106666564],
#   [37.56907837, 127.08555024],
#   [37.569014, 127.070344],
#   [37.568597, 127.06818],
#   [37.56559316, 127.05576],
#   [37.56821, 127.04407],
#   [37.56822, 127.044732],
#   [37.56624917, 127.04420328],
#   [37.567822435, 127.04568922],
#   [37.566835292, 127.04574031],
#   [37.565129533, 127.0473239],
#   [37.569093775, 127.04777598],
#   [37.568881178, 127.03903734],
#   [37.566653123, 127.04275488],
#   [37.565071333, 127.0398581],
#   [37.56803, 127.03265],
#   [37.5653, 127.03475445],
#   [37.56506, 127.03313],
#   [37.56684871, 127.03400015],
#   [37.56759, 127.03447],
#   [37.565415888, 127.03742434],
#   [37.56773, 127.03111],
#   [37.566139068, 127.03115581],
#   [37.565567, 127.0316914],
#   [37.56645139, 127.02178727],
#   [37.56512357, 127.0170201],
#   [37.56535145, 127.02069649],
#   [37.56682, 127.017092],
#   [37.56754712, 127.01813313],
#   [37.56644898, 127.0119162],
#   [37.56836018, 127.01048308],
#   [37.56862, 127.014787],
#   [37.569043, 127.011648],
#   [37.56710187, 127.01214106],
#   [37.56881307, 127.00877499],
#   [37.56859457, 127.00775925],
#   [37.567805, 127.005067],
#   [37.56921838, 127.00195247],
#   [37.56912618, 127.00222011],
#   [37.56740014, 127.00352062],
#   [37.56615038, 126.9957824],
#   [37.56517035, 126.9954911],
#   [37.56626933, 126.9953819],
#   [37.56568137, 126.99829135],
#   [37.56612307, 126.99559351],
#   [37.5683313, 126.9956424],
#   [37.56827, 126.995075],
#   [37.566153, 126.997339],
#   [37.568689, 126.994708],
#   [37.56896653, 126.99751818],
#   [37.56837721, 126.99794649],
#   [37.565641, 126.992781],
#   [37.56901932, 126.98920432],
#   [37.56753601, 126.98849319],
#   [37.56831662, 126.9893367],
#   [37.567672, 126.989318],
#   [37.56572319, 126.98872568],
#   [37.56466, 127.084522],
#   [37.56229166, 127.0671915],
#   [37.5617818, 127.06705264],
#   [37.563459744, 127.05530226],
#   [37.563808429, 127.05611228],
#   [37.562385913, 127.05569544],
#   [37.56180365, 127.05525815],
#   [37.56340931, 127.05604091],
#   [37.56064519, 127.0567091],
#   [37.56328524, 127.05628296],
#   [37.564765176, 127.05003976],
#   [37.56161106, 127.0518833],
#   [37.56458022, 127.05432169],
#   [37.560745, 127.04879],
#   [37.56367, 127.04215],
#   [37.5636, 127.03874],
#   [37.562606, 127.032796],
#   [37.56205, 127.03303],
#   [37.564542348, 127.03549],
#   [37.560946617, 127.03450441],
#   [37.562091, 127.037925],
#   [37.56083, 127.03043],
#   [37.5625999, 127.0176766],
#   [37.56137409, 127.01900035],
#   [37.56204618, 127.01442718],
#   [37.564729, 127.000972],
#   [37.56463752, 127.00142678],
#   [37.56379141, 126.99979555],
#   [37.5634183, 126.9961205],
#   [37.56440034, 126.99357536],
#   [37.559645, 127.168587],
#   [37.556923, 127.0811808],
#   [37.557336, 127.077946],
#   [37.559330686, 127.07301557],
#   [37.557880233, 127.07211106],
#   [37.56016, 127.048561],
#   [37.5585, 127.03941],
#   [37.55997427, 127.03930182],
#   [37.55715486, 127.04012516],
#   [37.558574351, 127.03574305],
#   [37.55906169, 127.03298455],
#   [37.556314, 127.038052],
#   [37.56028, 127.02835],
#   [37.55987, 127.02966],
#   [37.560316, 127.027944],
#   [37.55634366, 127.01597608],
#   [37.5562788, 127.0128583],
#   [37.55789144, 127.01270923],
#   [37.55897429, 127.01340538],
#   [37.5590781, 127.002698],
#   [37.5601902, 127.002238],
#   [37.56001, 127.00131646],
#   [37.56005799, 126.99316078],
#   [37.55660191, 126.99589418],
#   [37.559821, 126.989076],
#   [37.55292409, 127.15748447],
#   [37.55183962, 127.15475428],
#   [37.55459836, 127.15409092],
#   [37.55361065, 127.15591212],
#   [37.5540192, 127.1560139],
#   [37.55237413, 127.13512275],
#   [37.55289, 127.1377215],
#   [37.55188775, 127.08723617],
#   [37.552018, 127.078459],
#   [37.553013, 127.067656],
#   [37.55572095, 127.06986499],
#   [37.55384954, 127.04829171],
#   [37.552156381, 127.03658044],
#   [37.55402998, 127.03167662],
#   [37.55366, 127.02757],
#   [37.55243282, 127.02893614],
#   [37.5524, 127.0316],
#   [37.55457, 127.02715],
#   [37.551573, 127.026326],
#   [37.555579891, 127.01724708],
#   [37.55169, 127.01771],
#   [37.5535238, 127.01795732],
#   [37.552314, 127.019668],
#   [37.555595, 127.019728],
#   [37.55222214, 127.01335763],
#   [37.5556884, 127.0066239],
#   [37.56847403, 126.98608025],
#   [37.55923691, 126.98562404],
#   [37.567448, 126.985157],
#   [37.568395, 126.98235],
#   [37.5604002, 126.979568],
#   [37.55595263, 126.97934717],
#   [37.55631925, 126.98415243],
#   [37.55495673, 126.98173292],
#   [37.56342589, 126.98293645],
#   [37.567908, 126.979967],
#   [37.56733736, 126.98343453],
#   [37.56472646, 126.98096695],
#   [37.56983402, 126.98150586],
#   [37.571631, 126.983431],
#   [37.55519966, 126.98374278],
#   [37.560122, 126.982947],
#   [37.560362, 126.98095432],
#   [37.56392121, 126.98018973],
#   [37.57045278, 126.98383892],
#   [37.57267337, 126.98104937],
#   [37.568338, 126.982009],
#   [37.56337305, 126.98083219],
#   [37.55384119, 126.97579392],
#   [37.5547328, 126.9744666],
#   [37.5581731, 126.976018],
#   [37.55952, 126.975908],
#   [37.55953, 126.975731],
#   [37.56096448, 126.97813425],
#   [37.559468, 126.974095],
#   [37.55458553, 126.97798499],
#   [37.568228, 126.97805],
#   [37.563026, 126.975362],
#   [37.561784, 126.974236],
#   [37.56658706, 126.97825111],
#   [37.5677975, 126.978343],
#   [37.55631344, 126.97560042],
#   [37.564168, 126.978553],
#   [37.564181, 126.977563],
#   [37.561736, 126.973109],
#   [37.561078, 126.97227539],
#   [37.565593, 126.968315],
#   [37.56750993, 126.97089851],
#   [37.557744, 126.968618],
#   [37.555936, 126.970221],
#   [37.5590136, 126.9624063],
#   [37.558746, 126.9642899],
#   [37.56188747, 126.96337537],
#   [37.56531, 126.967965],
#   [37.55559696, 126.96497303],
#   [37.559389, 126.966214],
#   [37.552856, 126.949343],
#   [37.556123, 126.945195],
#   [37.551022, 126.936452],
#   [37.5610711, 126.939164],
#   [37.554134, 126.934784],
#   [37.55473789, 126.93943744],
#   [37.55631688, 126.93456352],
#   [37.55621008, 126.93582104],
#   [37.55675658, 126.92856417],
#   [37.553711, 126.934128],
#   [37.558325, 126.926802],
#   [37.55883346, 126.92738241],
#   [37.557095, 126.927441],
#   [37.55349117, 126.92431124],
#   [37.554439, 126.921297],
#   [37.557173, 126.918598],
#   [37.56016449, 126.92085666],
#   [37.56376056, 126.90835345],
#   [37.559577, 126.906609],
#   [37.564801, 126.906726],
#   [37.56633524, 126.90189819],
#   [37.564641, 126.903576],
#   [37.55558459, 126.90587312],
#   [37.557769, 126.901535],
#   [37.565454, 126.903534],
#   [37.561969, 126.905229],
#   [37.5651631, 126.89797706],
#   [37.556025, 126.900057],
#   [37.553965, 126.896929],
#   [37.569477, 126.8947403],
#   [37.56833, 126.89859],
#   [37.5613576, 126.88728016],
#   [37.56033753, 126.85977547],
#   [37.559486, 126.857267],
#   [37.559234, 126.857549],
#   [37.559112, 126.856912],
#   [37.557888, 126.856062],
#   [37.562073, 126.852591],
#   [37.561606, 126.853345],
#   [37.56332959, 126.85308175],
#   [37.562578, 126.853005],
#   [37.564269, 126.850032],
#   [37.558393, 126.855058],
#   [37.55998779, 126.84037793],
#   [37.558533, 126.842206],
#   [37.57155732, 126.84165292],
#   [37.568517, 126.839457],
#   [37.561364, 126.837048],
#   [37.559596, 126.832672],
#   [37.560423, 126.834402],
#   [37.558435, 126.834315],
#   [37.558168, 126.828561],
#   [37.558244, 126.827409],
#   [37.558933, 126.82384],
#   [37.558938, 126.824943],
#   [37.56706812, 126.81757628],
#   [37.57224302, 126.80518976],
#   [37.558348, 126.807332],
#   [37.554713, 126.809034],
#   [37.572006, 126.807753],
#   [37.560122, 126.804257],
#   [37.56471, 126.79971505],
#   [37.564851, 126.802117],
#   [37.564119, 126.803464],
#   [37.54738352, 127.00269901],
#   [37.547386, 126.960882],
#   [37.543023, 126.951226],
#   [37.546364, 126.953287],
#   [37.545954, 126.953002],
#   [37.54244058, 126.95338137],
#   [37.5438757, 126.95009648],
#   [37.54199792, 126.94523726],
#   [37.545996, 126.932496],
#   [37.545234, 126.909896],
#   [37.545722, 126.911222],
#   [37.54489139, 126.89289421],
#   [37.544613, 126.837163],
#   [37.53952176, 127.00257963],
#   [37.540206, 126.969997],
#   [37.541842, 126.949689],
#   [37.54155295, 126.94993374],
#   [37.54133579, 126.9489866],
#   [37.538408, 126.94504],
#   [37.53890027, 126.94266859],
#   [37.53796609, 126.90331806],
#   [37.5388433, 126.90146242],
#   [37.54149243, 126.84439601],
#   [37.53758251, 126.83934816],
#   [37.533664, 126.994379],
#   [37.53496611, 127.00019178],
#   [37.53713406, 126.9692661],
#   [37.53386, 126.96795],
#   [37.53436379, 126.96541818],
#   [37.53312255, 126.91729473],
#   [37.53679354, 126.8806468],
#   [37.53545727544941, 126.87807944929126],
#   [37.5372826680732, 126.88113087040016],
#   [37.53302124, 126.83625423],
#   [37.53504594, 126.82414512],
#   [37.529486, 126.97003],
#   [37.52917153, 126.96843137],
#   [37.528694, 126.963766],
#   [37.532138, 126.961445],
#   [37.528797, 126.931198],
#   [37.530037, 126.926235],
#   [37.529664, 126.924537],
#   [37.53240356, 126.924436],
#   [37.53261905, 126.90086754],
#   [37.532719, 126.9005],
#   [37.52853206, 126.89149431],
#   [37.528464, 126.89437002],
#   [37.531871, 126.875505],
#   [37.52937002, 126.87612377],
#   [37.530284, 126.873283],
#   [37.5240936, 126.9298043],
#   [37.52497241, 126.92532318],
#   [37.52407584, 126.92604709],
#   [37.524501, 126.923781],
#   [37.52607331, 126.92831446],
#   [37.52406, 126.924518],
#   [37.526097, 126.913163],
#   [37.52824898, 126.90779447],
#   [37.52782182, 126.90463093],
#   [37.526684, 126.902742],
#   [37.525797, 126.902025],
#   [37.52552609, 126.89579413],
#   [37.52625065, 126.89945376],
#   [37.52603084, 126.89527071],
#   [37.52432737, 126.89548892],
#   [37.527596, 126.896019],
#   [37.52606684, 126.89166568],
#   [37.52579977, 126.88797228],
#   [37.52790955709728, 126.87469438548555],
#   [37.52685813, 126.87503705],
#   [37.527005, 126.863928],
#   [37.525643, 126.837692],
#   [37.520253, 126.939938],
#   [37.52217837, 126.93973139],
#   [37.52249148, 126.93704902],
#   [37.52169298376825, 126.92284405231476],
#   [37.51947074, 126.90260898],
#   [37.520883, 126.869091],
#   [37.522184, 126.869169],
#   [37.521777, 126.869513],
#   [37.52037416777665, 126.868873716548],
#   [37.521383, 126.857487],
#   [37.52379759, 126.85141746],
#   [37.521433, 126.846456],
#   [37.51770458, 126.99191955],
#   [37.518577, 126.983287],
#   [37.51535432, 126.98314157],
#   [37.5174522, 126.97059677],
#   [37.51696501, 126.93576386],
#   [37.519058, 126.927645],
#   [37.51775234, 126.91460391],
#   [37.51597645, 126.90749608],
#   [37.51815768, 126.91153056],
#   [37.517985, 126.902785],
#   [37.516095, 126.899927],
#   [37.518244, 126.895921],
#   [37.51631443, 126.8877957],
#   [37.51796698162113, 126.86650968602822],
#   [37.515405, 126.862724],
#   [37.51527798956388, 126.8610298457858],
#   [37.516409, 126.862116],
#   [37.516978, 126.863605],
#   [37.516179, 126.861337],
#   [37.51687019364009, 126.86508588159528],
#   [37.513555, 127.003245],
#   [37.512823, 126.941669],
#   [37.512291, 126.925784],
#   [37.51332538, 126.91407775],
#   [37.51356811, 126.89715171],
#   [37.512193, 126.897016],
#   [37.513034, 126.850433],
#   [37.50967919, 126.99514709],
#   [37.50760295, 126.9628339],
#   [37.50769977, 126.96331901],
#   [37.50631944, 126.9406907],
#   [37.506728, 126.941458],
#   [37.5064277, 126.9350866],
#   [37.50834696, 126.89679637],
#   [37.506985, 126.890335],
#   [37.508607, 126.888938],
#   [37.50566233, 126.9801074],
#   [37.502399, 126.940339],
#   [37.50439719, 126.92088932],
#   [37.50563, 126.910559],
#   [37.503287, 126.881119],
#   [37.50329395, 126.87434357],
#   [37.504707, 126.870315],
#   [37.49814931, 126.99783192],
#   [37.49715663, 126.99877889],
#   [37.500311, 126.91664],
#   [37.49965667, 126.89483844],
#   [37.50085864, 126.88604808],
#   [37.50114707, 126.8827651],
#   [37.49747916, 126.86315996],
#   [37.497554, 126.855719],
#   [37.497803, 126.860705],
#   [37.493829, 126.924501],
#   [37.49314103, 126.90163365],
#   [37.49374143, 126.89514931],
#   [37.4928472, 126.89433148],
#   [37.49660657, 126.89348195],
#   [37.49510602, 126.89186155],
#   [37.494119, 126.89378],
#   [37.49296464, 126.88270317],
#   [37.49444763, 126.84103669],
#   [37.48895873, 126.99232981],
#   [37.490654, 127.005473],
#   [37.4891104, 126.92911787],
#   [37.49055258, 126.92509617],
#   [37.49039184, 126.92340595],
#   [37.492012, 126.924303],
#   [37.491212, 126.924987],
#   [37.48830327, 126.91452278],
#   [37.4917248, 126.884062],
#   [37.48968656, 126.88695201],
#   [37.49202674, 126.82393812],
#   [37.48549233, 126.99247595],
#   [37.483706, 126.973835],
#   [37.486163, 126.958534],
#   [37.48615857, 126.94738402],
#   [37.48386679, 126.93020739],
#   [37.48543179, 126.90124331],
#   [37.48481135, 126.90323392],
#   [37.48515535, 126.89507102],
#   [37.486037, 126.894718],
#   [37.486919, 126.895235],
#   [37.487319, 126.894567],
#   [37.487507, 126.894005],
#   [37.484386, 126.893324],
#   [37.48671161, 126.85769069],
#   [37.48728845, 126.83918316],
#   [37.486598, 126.838248],
#   [37.481083, 126.97161],
#   [37.48016976, 126.8952706470708],
#   [37.482417, 126.897046],
#   [37.482225, 126.895367],
#   [37.48307, 126.897861],
#   [37.48346092, 126.89654064],
#   [37.480802, 126.892895],
#   [37.48153894, 126.89345807],
#   [37.47944415, 126.88459482],
#   [37.48169755, 126.88484394],
#   [37.479934, 126.882532],
#   [37.482971, 126.878859],
#   [37.48018615, 126.88106079],
#   [37.48291585, 126.88115699],
#   [37.48039, 126.875947],
#   [37.48119476, 126.8760601],
#   [37.47984151, 126.87708848],
#   [37.48248593, 126.87746904],
#   [37.480874, 126.839309],
#   [37.47543791, 126.98377372],
#   [37.476133, 126.978907],
#   [37.477607, 126.889162],
#   [37.47723596, 126.88376012],
#   [37.47596366, 126.88840141],
#   [37.47820076, 126.88711812],
#   [37.47867559, 126.88639434],
#   [37.4784765, 126.88501587],
#   [37.47814, 126.881721],
#   [37.478802, 126.822703],
#   [37.476611, 126.81735],
#   [37.471474, 126.982437],
#   [37.474325, 126.917867],
#   [37.47065964, 126.89577553],
#   [37.47287815, 126.88323063],
#   [37.47145803, 126.88237814],
#   [37.47300896, 126.88113448],
#   [37.469384, 126.898483],
#   [37.46893342, 126.89572924],
#   [37.468669, 126.896874],
#   [37.46660227, 126.89009808],
#   [37.46602736, 126.8875314],
#   [37.466759, 126.886899],
#   [37.468397, 126.88777],
#   [37.46620821, 126.88710329],
#   [37.46684598, 126.88833083],
#   [37.462917, 126.905718],
#   [37.464592, 126.890806],
#   [37.46538608, 126.88749939],
#   [37.46077721, 126.91096477],
#   [37.461029, 126.89633],
#   [37.4592374, 126.8970595],
#   [37.45601954, 126.88759789],
#   [37.451886, 126.900804],
#   [37.63800702, 126.91932176],
#   [37.6374717811, 126.91783905],
#   [37.611843, 126.92932],
#   [37.607239, 126.934435],
#   [37.601228, 126.924603],
#   [37.60079507, 126.92066234],
#   [37.60431077, 126.92167204],
#   [37.587104, 126.883357],
#   [37.58522128, 126.81982059],
#   [37.57951713, 126.98059114],
#   [37.57970504, 126.89280744],
#   [37.57840939, 126.89298914],
#   [37.57858093, 126.89427368],
#   [37.58139385, 126.887447],
#   [37.58162041, 126.88706131],
#   [37.57542635, 126.9801813],
#   [37.576926, 126.9791106],
#   [37.57449014, 126.97418586],
#   [37.574719, 126.979023],
#   [37.577281, 126.897236],
#   [37.57730116, 126.81331479],
#   [37.57757395, 126.81217459],
#   [37.57798421, 126.79821222],
#   [37.57340269, 126.97588429],
#   [37.54991985, 127.17592213],
#   [37.54976664, 127.17440477],
#   [37.55097027, 127.14292219],
#   [37.551184, 127.110972],
#   [37.550808, 127.09759],
#   [37.55093306, 127.07649254],
#   [37.550354126, 127.06837751],
#   [37.550551, 127.067161],
#   [37.549976, 127.0680728],
#   [37.54887732, 127.06327915],
#   [37.549574824, 127.06457197],
#   [37.551250507, 127.06615984],
#   [37.5487, 127.05536127],
#   [37.54913662, 127.05519826],
#   [37.55074865727688, 127.05020070075987],
#   [37.55014473098784, 127.050222158432],
#   [37.55066359753223, 127.05024361610413],
#   [37.5494, 127.0518],
#   [37.550820957, 127.04624712],
#   [37.550255309, 127.04538345],
#   [37.549511028, 127.04634368],
#   [37.54866891869198, 127.04750776290892],
#   [37.5486300809474, 127.04114608441368],
#   [37.54982, 127.041794],
#   [37.549464244, 127.03298091],
#   [37.549237, 127.033572],
#   [37.54994909, 127.02660799],
#   [37.55082911, 127.02632265],
#   [37.55087391, 127.02336887],
#   [37.54896, 127.01793],
#   [37.54968115, 127.01962878],
#   [37.54569237, 127.14227409],
#   [37.544695, 127.136656],
#   [37.54524688, 127.11991897],
#   [37.54482977, 127.12189925],
#   [37.5455346, 127.0850851],
#   [37.545989, 127.0739607],
#   [37.54620633, 127.06341326],
#   [37.54742, 127.06253],
#   [37.54601, 127.06187],
#   [37.54574, 127.05851],
#   [37.5479718, 127.05989],
#   [37.5464, 127.06045],
#   [37.545576848, 127.05996],
#   [37.54452, 127.05846],
#   [37.544130719, 127.05642342],
#   [37.54740371784213, 127.04962118328592],
#   [37.54819, 127.05135405],
#   [37.54808, 127.05362],
#   [37.54659, 127.05106],
#   [37.5453, 127.05007],
#   [37.545614, 127.052007],
#   [37.545479022, 127.0505172],
#   [37.54445, 127.05445],
#   [37.547178, 127.050013],
#   [37.54422641973328, 127.0544761419296],
#   [37.545839, 127.045891],
#   [37.544292346, 127.0470947],
#   [37.54677201040518, 127.0472341775894],
#   [37.54587032406914, 127.0472127199173],
#   [37.547753, 127.045195],
#   [37.545295, 127.043045],
#   [37.546874087, 127.02728588],
#   [37.5484862, 127.0232804],
#   [37.5473207, 127.01593307],
#   [37.544193, 127.016471],
#   [37.54435, 127.0169],
#   [37.542974, 127.132245],
#   [37.54053, 127.134109],
#   [37.54131025, 127.12594022],
#   [37.540584, 127.125039],
#   [37.541306, 127.116449],
#   [37.54069, 127.082013],
#   [37.54043859, 127.07212746],
#   [37.54064061, 127.07017995],
#   [37.5402418, 127.0625534],
#   [37.543821505, 127.0608382],
#   [37.54265418, 127.06185],
#   [37.54246, 127.06102609],
#   [37.5399746, 127.06039855],
#   [37.542297497, 127.05991029],
#   [37.54314, 127.0588],
#   [37.54207, 127.05925],
#   [37.541721, 127.058677],
#   [37.541901923, 127.05103218],
#   [37.541200094, 127.05371975],
#   [37.5439, 127.05278],
#   [37.543620313, 127.04537272],
#   [37.54235, 127.04897],
#   [37.54006, 127.04911],
#   [37.54017, 127.04673],
#   [37.54314, 127.04659],
#   [37.5420109, 127.044587],
#   [37.53996228, 127.04638485],
#   [37.54078374, 127.0487364],
#   [37.54249491, 127.01721255],
#   [37.541363, 127.018293],
#   [37.535495, 127.138683],
#   [37.536141, 127.135263],
#   [37.53722656, 127.13773854],
#   [37.538432, 127.137169],
#   [37.53516026, 127.13365501],
#   [37.53890256, 127.13325491],
#   [37.536952, 127.129914],
#   [37.53849749, 127.12512853],
#   [37.53886562, 127.12444339],
#   [37.53551936, 127.12029156],
#   [37.53604678, 127.11607498],
#   [37.5391245, 127.09138968],
#   [37.53702, 127.082943],
#   [37.537905, 127.076347],
#   [37.53867795, 127.06824343],
#   [37.53957343, 127.0593229],
#   [37.5394386, 127.0553073],
#   [37.53928655, 127.06004897],
#   [37.5379131, 127.05649422],
#   [37.53732077, 127.059491],
#   [37.536512557, 127.05679357],
#   [37.537979165, 127.05766797],
#   [37.5357232, 127.05734114],
#   [37.53716718, 127.05619675],
#   [37.53641, 127.04955],
#   [37.5383223, 127.0520354],
#   [37.53701025, 127.052308],
#   [37.53621904, 127.05255568],
#   [37.53609568, 127.0504367],
#   [37.535704332, 127.05192804],
#   [37.5374, 127.05428],
#   [37.535236407, 127.053532],
#   [37.535542685, 127.05442249],
#   [37.531248, 127.129855],
#   [37.5349417, 127.09125929],
#   [37.53090327, 127.08416216],
#   [37.53157639, 127.08647428],
#   [37.531674, 127.027216],
#   [37.53106835, 127.02481727],
#   [37.529346, 127.136281],
#   [37.530569, 127.12366237],
#   [37.52808559, 127.04159925],
#   [37.52857263, 127.0400765],
#   [37.526269, 127.028388],
#   [37.52761162, 127.03170913],
#   [37.52732583, 127.02746025],
#   [37.52701729, 127.02647115],
#   [37.5275464, 127.01895624],
#   [37.52231457, 127.10290327],
#   [37.52188443, 127.0409429],
#   [37.52381624, 127.03561265],
#   [37.52581394, 127.0283654],
#   [37.52309456, 127.02429256],
#   [37.51806624, 127.10505804],
#   [37.517984, 127.081214],
#   [37.52061352, 127.05741236],
#   [37.5175696, 127.04750582],
#   [37.51999434, 127.04565885],
#   [37.51828534, 127.04322537],
#   [37.51983461, 127.03339974],
#   [37.518087, 127.0293906],
#   [37.51829753, 127.02916516],
#   [37.51511711, 127.10725577],
#   [37.515711, 127.111169],
#   [37.51668888, 127.10343693],
#   [37.513214, 127.103274],
#   [37.51449368, 127.10073623],
#   [37.51427683, 127.10341414],
#   [37.51579103, 127.09910681],
#   [37.51504294, 127.06315005],
#   [37.51434435, 127.0626519],
#   [37.51405345, 127.06394076],
#   [37.5160902, 127.05208629],
#   [37.514637, 127.03033],
#   [37.515849, 127.020618],
#   [37.51419673, 127.02060837],
#   [37.51142084, 127.09804531],
#   [37.5091049, 127.08647786],
#   [37.51141972, 127.0799307],
#   [37.50849, 127.066681],
#   [37.50929417, 127.06640733],
#   [37.51142444, 127.06509668],
#   [37.51243164, 127.05884715],
#   [37.50861623, 127.05973996],
#   [37.511048, 127.058108],
#   [37.5102479, 127.04645828],
#   [37.50822463, 127.02626245],
#   [37.512067, 127.023648],
#   [37.511022, 127.023183],
#   [37.509251, 127.00751007],
#   [37.503758, 127.126885],
#   [37.50642656, 127.11780965],
#   [37.50704487, 127.11336408],
#   [37.5063778, 127.10851738],
#   [37.50633272, 127.06815131],
#   [37.50707261, 127.06228028],
#   [37.50618013, 127.06374105],
#   [37.50752506, 127.05676928],
#   [37.505903, 127.055303],
#   [37.50527179, 127.05289807],
#   [37.505885, 127.052161],
#   [37.50475364, 127.05103466],
#   [37.50687927, 127.05243354],
#   [37.506041, 127.049017],
#   [37.50486336, 127.01835867],
#   [37.50474149, 127.02098179],
#   [37.500309, 127.154955],
#   [37.503081, 127.125325],
#   [37.499804, 127.111493],
#   [37.50039737, 127.10408468],
#   [37.50025109, 127.09589543],
#   [37.502748, 127.067243],
#   [37.499395, 127.061136],
#   [37.50227954, 127.06420443],
#   [37.49997242, 127.06638144],
#   [37.501437, 127.054344],
#   [37.50346366, 127.04987204],
#   [37.50352939, 127.04707528],
#   [37.503222, 127.047242],
#   [37.50351, 127.041761],
#   [37.503416, 127.042847],
#   [37.502116, 127.039836],
#   [37.49998021, 127.0359282],
#   [37.500036, 127.03217],
#   [37.5026327, 127.03006081],
#   [37.49528691901275, 127.15556077987078],
#   [37.49615427, 127.14984862],
#   [37.495187, 127.150971],
#   [37.49495555, 127.07932368],
#   [37.49705092, 127.07239543],
#   [37.494774, 127.061865],
#   [37.49782255, 127.05648634],
#   [37.496258, 127.05174035],
#   [37.49906096, 127.05468508],
#   [37.496953, 127.053346],
#   [37.498518, 127.047981],
#   [37.49534845, 127.03323757],
#   [37.498702, 127.03163],
#   [37.49436437, 127.1561092],
#   [37.4930504, 127.149032],
#   [37.493986, 127.116099],
#   [37.49109045, 127.08731671],
#   [37.49403327, 127.087416],
#   [37.49192117, 127.08129163],
#   [37.49461857, 127.07115188],
#   [37.49360041, 127.06327573],
#   [37.49250002, 127.0388068],
#   [37.493762, 127.043149],
#   [37.494383, 127.027711],
#   [37.490875, 127.030305],
#   [37.494023, 127.028388],
#   [37.492016, 127.009657],
#   [37.485798, 127.142556],
#   [37.48599491, 127.12464869],
#   [37.48801285, 127.09994995],
#   [37.48948769, 127.08176548],
#   [37.48949036, 127.06623841],
#   [37.48867108, 127.05302777],
#   [37.48664435, 127.03705039],
#   [37.48998528, 127.02969202],
#   [37.48895165, 127.0079434],
#   [37.48795025, 127.00893688],
#   [37.484172, 127.121364],
#   [37.48468629, 127.08408987],
#   [37.48150119, 127.04781332],
#   [37.484765, 127.045972],
#   [37.48430646, 127.04341808],
#   [37.48327278, 127.02113395],
#   [37.485691, 127.02075],
#   [37.477592206, 127.125068],
#   [37.47725982, 127.06647741],
#   [37.47791276, 127.06605468],
#   [37.47967132, 127.03967212],
#   [37.47354638, 127.11441141],
#   [37.47564571, 127.05236496],
#   [37.4723039, 127.03822651],
#   [37.47005293, 127.1277329],
#   [37.47129437, 127.11917805],
#   [37.472022, 127.09604],
#   [37.471637, 127.048511],
#   [37.47009388, 127.04432613],
#   [37.47217874, 127.04431809],
#   [37.466035, 127.101406],
#   [37.46445115, 127.10558271],
#   [37.467241, 127.099975],
#   [37.46331731, 127.03687065],
#   [37.457159, 127.058727],
#   [37.44735, 127.056302],
#   [37.44792, 127.055722],
# ]

# Headers configuration
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,zh;q=0.6",
    "connection": "keep-alive",
    "content-length": "77",  # Normally not required to be set manually in `requests`
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    # "cookie": (
    #     "WL_PCID=17261862247686803879572; _ga_13TFLYF8E5=GS1.1.1726189246.2.1.1726189248.58.0.708873100; "
    #     "_ga=GA1.1.1394327740.1726186225; _ga_7E3SHQ0N26=GS1.1.1727063525.1.1.1727063536.49.0.0; "
    #     "_ga_TQ9XZMS9KQ=GS1.1.1727063524.1.1.1727063536.48.0.0; dable_uid=67394682.1726213305857; "
    #     "_SSO_Global_Logout_url=get%5Ehttps%3A%2F%2Fwww.seoul.go.kr%2Fmember%2Fuserlogin%2FlogOut.do%24get%5Ehttp%3A%2F%2Fdata.seoul.go.kr%2Fsso%2Flogout.jsp%3Flogout%3D1%24; "
    #     "_ga_7BKNBL2WLX=GS1.1.1727159416.2.0.1727159417.0.0.0; JSESSIONID=3ba8EcnVUyzABV5Eya5Bgl7TaZuv6yKDBMWlD3tl4cv8UnFqzrasiTLT9fckPojN.amV1c19kb21haW4vbWVtYmVyMTA1; "
    #     "_ga_0T3XG23CN7=GS1.1.1727427152.16.0.1727427152.60.0.0; JSESSIONID=4770138BAEB2D5FC158DDA2F53750C0B"
    # ),
    "host": "parking.seoul.go.kr",
    "origin": "https://parking.seoul.go.kr",
    "referer": "https://parking.seoul.go.kr/",
    "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0"
}

# URL to fetch parking data
url = "https://parking.seoul.go.kr/SearchParking.do"
range_value = 100

# Set to store unique parking names

# List to store collected parking data
# total_filter_data = []

def save_to_firebase(data):
  with open(f'./parking_data/{time.time()}.json', 'w') as json_file:
      json.dump(data, json_file, ensure_ascii=False)
def fetch_parking_data():
    total_filter_data = []
    added_parking_names = set()

    for count, (lat, lon) in enumerate(demo):
        # Payload configuration
        payload = {
            'LAT': str(lat),
            'LON': str(lon),
            'range': str(range_value)
        }

        # Send POST request to fetch parking data
        try:
            response = requests.post(url, headers=headers, data=payload, verify=False)
            response_data = response.json()
            parking_list = response_data.get('res_value', {}).get('parking_list', [])
            time.sleep(random.randint(1,10)/5)
            print(f"RequestTime: {time.strftime('%Y-%m-%d %H:%M:%S')}  TargetIndex: {count}")
            # Filter and store parking data
            for parking in parking_list:
              parking_name = parking.get('parking_name')
              try:
                capacity = int(parking.get('capacity', 0))
                cur_parking = int(parking.get('cur_parking', 0))
                available_parking = capacity - cur_parking
              except ValueError:
                available_parking = None  
              if parking.get('que_status_nm') != "미연계" and parking_name not in added_parking_names :
                  added_parking_names.add(parking['parking_name'])
                  parking_info = {
                        "주차장 이름": f"{parking.get('parking_name')}",
                        "주소": f"{parking.get('address')}",
                        "새 주소": f"{parking.get('new_juso')}",
                        "주차 타입": parking.get('parking_type'),
                        "전체 주차 면": capacity,
                        "현재 주차 차량 수": cur_parking,
                        "주차 가능 면":  available_parking,
                        "요금": f"{parking.get('rates')}원/{parking.get('time_rate')}분",
                        "추가 요금": f"{parking.get('add_rates')}원",
                        "요금 부과 기준": f"{parking.get('time_rate')}분",
                        "정기권 요금": f"{parking.get('fulltime_monthly')}원",
                        "일일 최대 요금": f"{parking.get('day_maximum')}원",
                        "현재 주차 갱신 시간": parking.get('cur_parking_time'),
                        "평일 운영 시간": f"{parking.get('weekday_begin_time')} ~ {parking.get('weekday_end_time')}",
                        "주말 운영 시간": f"{parking.get('weekend_begin_time')} ~ {parking.get('weekend_end_time')}",
                        "공휴일 운영 시간": f"{parking.get('holiday_begin_time')} ~ {parking.get('holiday_end_time')}",
                        "전화번호": parking.get('phone'),
                        "연계 상태": parking.get('que_status_nm'),
                        "위치 정보": [(position.get('lat'), position.get('lng')) for position in parking.get('position_list', [])],
                        "count": count,
                        "date": time.time()
                    }
                  total_filter_data.append(parking_info)

        except Exception as e:
            print(f"Error fetching parking data: {e}, \n count: {count}")
            continue

    # Save collected data to Firebase
    save_to_firebase(total_filter_data)

# Call the function to fetch and save parking data

start_time = time.time()
fetch_parking_data()
while True:
    time.sleep(0.5)
    chek_time = time.time()
    if int(chek_time - start_time) > 1200:
      fetch_parking_data()
      start_time = chek_time # 시간을 다시 초기화