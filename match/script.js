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


function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]]; // 交换
    }
}

const totalWords = 4;

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
    newMap = getRandomSubmap(fruitMap, totalWords)
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
        button.onclick = () => wordClicked(word, 'chinese', button); // 将按钮元素也传递给wordClicked函数
        chineseContainer.appendChild(button);
    });

    englishWords.forEach(word => {
        const button = document.createElement('button');
        button.textContent = word;
        button.className = 'button';
        button.onclick = () => wordClicked(word, 'english', button); // 将按钮元素也传递给wordClicked函数
        englishContainer.appendChild(button);
    });
}

let selectedWords = [];
let matchCount = 0;
function checkMatch() {
    const selected = [...selectedWords]; // 保存对selectedWords的引用
    selectedWords = []; // 立即重置selectedWords数组
    
    const [firstButton, secondButton] = selected;
    if (firstButton.language === secondButton.language) {
        alert('请选择不同语言的单词！');
        resetButtonColor(firstButton);
        resetButtonColor(secondButton);
    } else {
        const chineseWord = firstButton.language === 'chinese' ? firstButton.word : secondButton.word;
        if (fruitMap[chineseWord] === (firstButton.language === 'english' ? firstButton.word : secondButton.word)) {
            matchCount++;
            firstButton.element.style.backgroundColor = 'green';
            secondButton.element.style.backgroundColor = 'green';
            
            if (matchCount === totalWords) {
                alert('全部匹配成功！');
                matchCount = 0;
                generateWords();
            }
        } else {
            alert('匹配失败，请重试！');
            resetButtonColor(firstButton);
            resetButtonColor(secondButton);
        }
    }
}

function resetButtonColor(button) {
    // 只有当按钮颜色不是绿色时才重置颜色
    if (button.element.style.backgroundColor !== 'green') {
        button.element.style.backgroundColor = '';
    }
}

function wordClicked(word, language, element) {
    // 如果按钮颜色已经是绿色，则不允许用户选择
    if (element.style.backgroundColor === 'green') {
        return;
    }
    
    selectedWords.push({ word, language, element }); // 将元素也传递到对象中
    element.style.backgroundColor = 'yellow'; // 当单词被选中时，改变按钮颜色为黄色
    if (selectedWords.length === 2) {
        checkMatch();
        selectedWords = [];
    }
}

window.onload = generateWords;
