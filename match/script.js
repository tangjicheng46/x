const fruitMap = {
    'あ':'a',
    'い':'i',
    'う':'u',
    'え':'e',
    'お':'o',
    'か':'ka',
    'き':'ki',
    'く':'ku',
    'け':'ke',
    'こ':'ko',
    'さ':'sa',
    'し':'shi',
    'す':'su',
    'せ':'se',
    'そ':'so',
    'た':'ta',
    'ち':'chi',
    'つ':'tsu',
    'て':'te',
    'と':'to',
    'な':'na',
    'に':'ni',
    'ぬ':'nu',
    'ね':'ne',
    'の':'no',
    'は':'ha',
    'ひ':'hi',
    'ふ':'fu',
    'へ':'he',
    'ほ':'ho',
    'ま':'ma',
    'み':'mi',
    'む':'mu',
    'め':'me',
    'も':'mo',
    'や':'ya',
    'ゆ':'yu',
    'よ':'yo',
    'ら':'ra',
    'り':'ri',
    'る':'ru',
    'れ':'re',
    'ろ':'ro',
    'わ':'wa',
    'を':'wo',
    'ん':'n'
};

let selectedWords = [];

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]]; // 交换
    }
}

function getRandomSubmap(map, n) {
    const keys = Object.keys(map);
    const shuffledKeys = keys.sort(() => Math.random() - 0.5);
    const newMap = {};
    
    for (let i = 0; i < n && i < shuffledKeys.length; i++) {
        const key = shuffledKeys[i];
        newMap[key] = map[key];
    }

    return newMap;
}


function generateWords() {
    newMap = getRandomSubmap(fruitMap, 4)
    const chineseWords = Object.keys(newMap);
    const englishWords = Object.values(newMap);

    shuffleArray(chineseWords);
    shuffleArray(englishWords);

    const chineseContainer = document.getElementById('chineseWords');
    const englishContainer = document.getElementById('englishWords');

    chineseContainer.innerHTML = '';
    englishContainer.innerHTML = '';

    chineseWords.forEach(word => {
        const button = document.createElement('button');
        button.textContent = word;
        button.className = 'button';
        button.onclick = () => wordClicked(word, 'chinese');
        chineseContainer.appendChild(button);
    });

    englishWords.forEach(word => {
        const button = document.createElement('button');
        button.textContent = word;
        button.className = 'button';
        button.onclick = () => wordClicked(word, 'english');
        englishContainer.appendChild(button);
    });
}

function checkMatch() {
    const [first, second] = selectedWords;
    if (first.language === second.language) {
        alert('请选择不同语言的单词！');
    } else {
        const chineseWord = first.language === 'chinese' ? first.word : second.word;
        if (fruitMap[chineseWord] === (first.language === 'english' ? first.word : second.word)) {
            alert('匹配成功！');
            generateWords();
        } else {
            alert('匹配失败，请重试！');
        }
    }
}

function wordClicked(word, language) {
    selectedWords.push({ word, language });
    if (selectedWords.length === 2) {
        checkMatch();
        selectedWords = [];
    }
}

window.onload = generateWords;
