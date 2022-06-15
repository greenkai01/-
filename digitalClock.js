const timeDiv = document.getElementById("clock");
const todayDiv = document.getElementById("today");


function getTime() {
  let now = new Date();
  let hour = number(now.getHours()); //시 0-23시
  let minute = number(now.getMinutes()); //분 0-59분
  let second = number(now.getSeconds()); //초 0-59초
  let noon = "오전";
  if (hour > 11) {
    noon = "오후";
    if(hour > 12) {
        hour = hour - 12;
    }
  }


  if (now.getHours() == 0) {
    hour = 12;
  }

  timeDiv.textContent = noon + " " + hour + "시 " + minute + "분 " + second + "초";
}


function getDate() {
  const date = new Date();
  const year = date.getFullYear();
  const month = date.getMonth()+1;
  const day = date.getDate();
  const dayNumber = date.getDay();
  const dayList = ["일","월","화","수","목","금","토"];
  const perfactDay=(dayList[date.getDay()]+'요일');

  todayDiv.textContent = year + "년 " + month + "월 " + day + "일 " + perfactDay;
}

getDate();

getTime();

setInterval(getTime, 1000);

function number(num) {
    if(num < 10){
        return "0" + num;
    }
    return num;
}