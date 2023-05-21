from zad6testy import runtests
from collections import deque


def update_path(path, S, T):
    # if len(path) > 2:
    #     print(path)
    for i in range(0, len(path), 2):
        S[path[i]] = path[i+1]
        T[path[i+1]] = path[i]


def poszerz(v, S, T, G):
    vis = [False]*len(G)
    q = deque()
    q.append((v, []))
    while len(q) > 0:
        v, path = q.popleft()
        vis[v] = True
        for u in G[v]:
            if T[u] is None:
                update_path(path+[v, u], S, T)
                return
            if not vis[T[u]]:
                q.append((T[u], path+[v, u]))


def binworker(G):
    n = len(G)
    # print(G)
    R = [None]*n
    T = [None]*n
    for i in range(n):
        poszerz(i, R, T, G)
    s = 0
    # print(T)
    for el in T:
        if el is not None:
            s += 1
    return s


M = [[195, 76], [438], [380], [318, 319], [475, 205, 158], [17, 370], [400, 10, 293], [216], [56, 54, 183], [454], [128, 121], [312, 393, 371], [11, 68], [24, 406, 479], [246], [296, 329, 10], [0, 277], [59], [177], [57, 11, 460], [131], [123, 397, 62], [409, 98, 443], [357, 142], [8, 185, 190], [456, 105, 294], [185, 212], [3], [217, 350, 103], [265, 494], [201, 234, 36], [92], [126], [400, 221], [347, 220], [74, 459], [81], [160, 357, 135], [448, 3], [416, 498, 451], [346, 163, 76], [242], [348], [464, 350, 423], [66, 299], [305, 110], [376, 17, 78], [146, 324, 37], [400], [258], [272], [374, 487], [1, 338, 239], [369, 122, 451], [289, 194], [308, 493], [443, 36, 381], [415], [57, 294, 399],
     [313, 366], [304], [158], [76], [152, 374, 351], [155, 366], [49, 238], [16, 402, 117], [220], [387, 156, 14], [218, 124, 471], [326], [88, 90, 357], [176, 98, 141], [152], [486], [264, 209], [347], [449, 379, 110], [129], [391], [43, 37, 182], [297, 482], [1, 388, 6], [400, 325], [480, 375], [458, 363], [273], [235], [405, 374, 295], [69], [360, 155], [430], [97, 130, 188], [64], [235, 54], [473, 346, 319], [153], [424, 499], [218, 308, 159], [434, 367], [314,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  131, 253], [281, 74], [120, 381], [87], [97, 418], [300, 133], [307, 444], [354, 100, 391], [222], [480, 277, 158], [468, 269], [96, 65, 271], [211], [9], [496, 427], [206, 311], [265], [227], [137, 18, 259], [265, 50, 247], [153, 42], [488, 410, 5], [488, 97], [401, 444, 247], [208, 237, 463], [57, 155, 372], [171], [173], [315, 484], [275, 246], [165, 6], [132, 189, 390], [164], [242, 83, 148], [74, 7], [193], [120, 109, 7], [231], [377, 290, 447], [153, 326], [448, 357, 6], [0, 461, 46], [240], [98, 223], [129, 94], [92], [395, 220, 166], [306, 19], [361, 498], [460, 125], [195, 28], [310, 31], [281], [484, 311], [90], [112, 461, 190], [348, 245], [280, 33, 171], [456, 49, 443], [112, 81, 319], [464, 399], [426, 155], [225, 130], [388, 317], [55], [253, 118], [449, 60], [419], [409], [448, 249, 227], [459, 148], [67, 78], [429, 174], [97, 42, 380], [96, 74, 141], [348], [290, 388, 175], [234], [73, 164], [16, 299],
     [10, 220, 271], [70], [264], [75, 318], [21], [367], [161], [67], [193, 203, 70], [353], [24, 459, 429], [484, 397, 199], [155], [485, 246, 351], [197], [227, 76], [234], [272, 249, 230], [460, 101], [328, 137, 143], [436, 405, 191], [171], [145, 3, 118], [145, 222], [416, 226, 405], [144, 101], [91, 412], [499, 398], [193, 466, 311], [445], [32, 275], [410, 367], [97, 62, 87], [66, 421, 351], [138, 357], [64], [458, 327], [393, 214], [121, 60], [288, 487], [104, 458, 363], [430], [180, 245, 38], [124, 125], [88, 147, 157], [32, 71], [142], [184, 173], [164, 415], [350, 7], [201, 43, 462], [225, 118], [248, 465], [451], [149], [379, 20, 461], [16, 431], [210], [320, 173], [400, 473, 291], [201, 212, 263], [184, 431], [158, 439], [241], [104, 491, 445], [384, 457, 235], [52, 375], [414], [124], [402, 407], [274, 203, 357], [125], [79], [241], [211], [145, 242, 175], [45], [275, 492], [428, 454, 7], [310, 359], [13, 246], [148, 109, 318], [480, 257], [363, 332, 437], [291], [245], [296, 41, 491], [115], [90, 149, 143], [241], [296, 341, 383], [95], [333, 430], [336, 137], [76, 5, 207], [371], [401], [105, 324, 103], [315], [210, 147, 461], [321, 106], [80], [338, 255], [213, 246, 119], [41, 155, 30], [490, 341], [156], [322, 167], [173, 230, 215], [401, 226], [332], [26, 476, 63], [102], [289, 324, 334], [180, 389, 134], [304], [82, 83], [321], [57, 388, 311], [191], [193], [216, 335], [270], [292], [435, 254], [385], [352, 61, 23], [423], [26, 165], [489, 52], [248, 451], [98, 491], [409], [499, 380], [210, 199], [333, 38, 343], [89, 418], [28, 61], [433, 307, 404], [399], [225, 58, 291], [45, 254], [153, 332], [0, 185, 83], [412, 175], [382], [32], [330, 428, 303], [90, 228, 15], [56, 106, 167], [211, 30], [427, 21, 318], [285, 150, 111], [417], [124, 239], [468, 286, 263], [50], [144], [67, 212, 46], [126], [252, 53, 390], [376, 445], [339, 220, 13], [468, 53, 135], [319], [69, 230, 55], [314, 493], [185, 180], [424, 103], [358, 255], [313, 34], [400], [480, 274, 127], [54], [488], [376, 282, 47], [470], [468, 21], [412, 373, 47], [403], [377, 494, 487], [69,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  430], [252], [486], [280, 85, 382], [328, 353], [371], [205, 334], [360, 361], [19], [445], [275], [385, 234, 275], [322, 349, 415], [273], [224, 19], [234, 19], [169, 162, 331], [385], [479], [113, 214], [289, 244], [167], [177, 174], [160, 434, 269], [64, 401], [163], [301], [428, 23], [426, 487], [258, 157], [256, 258, 69], [148], [259, 276, 422], [10, 15], [237, 358, 103], [181, 326], [320], [170, 487], [442, 173, 103], [113, 262], [68], [102], [177, 468], [32, 1, 351], [255], [361, 278], [200, 329], [304, 417, 183], [263], [433, 186, 351], [25], [256, 203], [194, 359], [217], [291, 252, 277], [348, 245, 199], [121, 308, 255], [289, 139, 76], [48, 27, 453], [24, 273, 311], [195, 356], [434], [34, 348, 429], [144, 325], [472, 363], [372, 366, 31], [272, 218, 219], [130, 340, 207], [466], [12], [126], [232], [32, 266, 139], [484, 286, 247], [210], [300, 189, 374], [76, 325], [251, 420, 93], [443], [141, 270, 431], [257], [444, 477, 39], [472, 11, 373], [320, 265, 211], [392, 119], [227, 334], [353], [328, 139], [346, 219], [145], [472, 213, 87], [423], [61], [415], [69, 14], [452], [214], [144, 485, 310], [424], [318], [104, 413], [251], [106, 355, 285], [465, 490, 147], [2, 181], [48], [130], [353, 452], [251, 196], [16, 234, 87], [194], [136, 258, 197], [448], [118], [57, 372], [187], [281, 419, 38], [418, 331, 149], [485], [24, 97, 211], [32, 1, 475], [35, 204], [82, 311], [461], [384, 3, 437], [368, 195, 477], [108, 269, 199], [348, 247], [458], [348], [146], [440], [262], [184, 473, 442], [360], [250, 51, 132], [18, 315], [445, 214, 391], [309, 382, 127]]
# sol 468

# M = [[0, 1, 3],
#      [2, 4],
#      [0, 2],
#      [3],
#      [3, 2]]
print(binworker(M))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker, all_tests=False)