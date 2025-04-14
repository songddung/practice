// 1. 변수
// let age = 29;
// age = 30;

// 2. 상수 == 불변, 초기화 필수
// const birth = "1997.04.01";

// 3. 변수 명명규칙(네이밍 규칙)
// 3-1. $, _ 제외한 기호는 사용X
// 3-2. 숫지로 시작x
// 3-3. 예약어 사용 x

// 4. 변수 명명 가이드


// 자료형
// 1. Number Type
let num1 = 29;
let num2 = 1.5;
let num3 = -20;

let inf = Infinity;
let mInf = -Infinity;

let nan = NaN;

// 2. String Type
let name = "송현광";
let myLocation = "첨단";
let introduce = name+myLocation;

let introduceText = `${name}은 ${myLocation}에 거주합니다`;
console.log(introduceText);

// 3. Boolean Type
let isSwitchOn = true;
let isEmpty = false;

// 4. null Type
let empty = null;


// 5. Undifined Type
let none;

// 연산자2
// 1. null 병합 연산자
let var1;
let var2 = 10;
let var3 = 20;

let var4 = var1 ?? var2;
let var5 = var1 ?? var3;
let var6 = var3 ?? var2;

// 2. typeof 연산자

let var7 = 1;
var7 = true;
var7 = "Hello";

// 3. 삼항연산자
let var8 = 10;
let res = var8 % 2 === 0 ? "짝수" : "홀수";


// 조건문
// 대표 : if, switch

// 1. if 조건문(if문)
let num = 9;

if(num >= 10) {
    // console.log("num은 10이상")
    // console.log("참");
} else if (num >= 5){
    // console.log("num은 3이상")
} else {
    // console.log("거짓");
}

// 2. Switch문
// if문과 기능 자체는 동일
// 다수의 조건을 처리할 때 if문 보다 직관적
let animal = "cat";

switch (animal) {
    case "cat": {
        console.log("고양이");
        break
    }
    case "dog": {
        console.log("개");
        break
    }
    case "bear": {
        console.log("곰");
        break
    }
    case "snake": {
        console.log("뱀");
        break
    }
    case "tiger": {
        console.log("호랑이");
        break
    }
    default: {
        console.log("모름");
    }
}

// 반복문
// for
for(let idx=0; idx<10; idx++) {
    console.log("반복");
}


// 함수
// 호이스팅 > 끌어올림 > 선언보다 호출이 위에 있어도 에러가 발생하지않음
function getArea(width, height) {
    let area = width * height;
    return area
}

let area1 = getArea(10,20)
console.log(area1);

// 함수 표현식
function funcA() {
    console.log("funcA");
}
let varA = funcA;
varA()

// 호이스팅 안됌 주의!
let varB = function () {
    console.log("funcB");
}
varB()

// 화살표 함수
let varC = (value) => {
    console.log(value);
    return value + 1;
};
console.log(varC(10))


// 콜백함수 (callback)
// 자신이 아닌 다른 함수에, 인수로써 전달된 함수를 의미
function main(value) {
    value();
}



main(() => {
    console.log("i am sub");
});

function repeat(count, callback) {
    for (let idx = 1; idx <= count; idx++){
        callback(idx);
    }
}


repeat(5, (idx) => {
    console.log(idx);
});

repeat(5, (idx) => {
    console.log(idx * 2);
});


// 스코프
// 우리말로 범위
// 변수나 함수에 접근하거나 호출할 수 있는 범위
// 전역 / 지역
// 전역 : 전체영역에서 접근 가능
// 지역 : 특정 영역에서만 접근 가능

let a = 1;

function funcA() {
    
}