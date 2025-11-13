$(document).ready(function(){
  var tema = localStorage.getItem('theme')
  if (tema === 'dark'){
    document.body.className = 'dark-theme';
    document.documentElement.setAttribute('data-bs-theme', 'dark');
    document.getElementById('phone').style.backgroundColor="black" ;
    document.getElementById('searchmenu').style.backgroundColor="#696969" ;
    document.getElementById("themeToggle").innerHTML = "Светлая тема";}

  else {
    document.body.className = 'light-theme';
    document.documentElement.setAttribute('data-bs-theme', 'ligth');
    document.getElementById('phone').style.backgroundColor="#f8f8f8" ;
    document.getElementById('searchmenu').style.backgroundColor="#f8f8f8" ;
    document.getElementById("themeToggle").innerHTML = "Тёмная тема";
    document.getElementsByClassName('text').style.color = "#ffffff";

  }
});


document.getElementById('themeToggle').addEventListener('click', function() {
    const currentTheme = document.body.className;
    if (currentTheme === 'light-theme') {
        document.body.className = 'dark-theme';
        document.documentElement.setAttribute('data-bs-theme', 'dark');
        document.getElementById('phone').style.backgroundColor="black" ;
        document.getElementById('searchmenu').style.backgroundColor="#696969" ;
        document.getElementById("themeToggle").innerHTML = "Светлая тема";
        localStorage.setItem('theme','dark' )


    } else {
        document.body.className = 'light-theme';
        document.documentElement.setAttribute('data-bs-theme', 'ligth');
        document.getElementById('phone').style.backgroundColor="#f8f8f8" ;
        document.getElementById('searchmenu').style.backgroundColor="#f8f8f8" ;
        document.getElementById("themeToggle").innerHTML = "Тёмная тема";
        localStorage.setItem('theme','ligth' )
    }
});


$(document).ready(function(){
    $(".search").keyup(function(){
        _this = this;
        $.each($("#table1 tbody tr"), function() {
            if($(this).text().toLowerCase().indexOf($(_this).val().toLowerCase()) === -1)
               $(this).hide();
            else
               $(this).show();
        });
    });
});


table1.onclick = function (e) {
  if (e.target.tagName != 'TH') return;
  let th = e.target;
  sortTable(th.cellIndex, th.dataset.type, 'table1');
};

function sortTable(colNum, type, id) {
  let elem = document.getElementById(id)
  let tbody = elem.querySelector('tbody');
  let rowsArray = Array.from(tbody.rows);
  let compare;
  switch (type) {
    case 'number':
      compare = function (rowA, rowB) {
        return rowA.cells[colNum].innerHTML - rowB.cells[colNum].innerHTML;
      };
      break;
    case 'string':
      compare = function (rowA, rowB) {
        return rowA.cells[colNum].innerHTML > rowB.cells[colNum].innerHTML ? 1 : -1;
      };
      break;
  }
  rowsArray.sort(compare);
  tbody.append(...rowsArray);
}

$('.name').on('click', function(){
  let fio = $(this).text()
  let photo = $(this).siblings('.photo').children('img')
  let mail = $(this).siblings('.mail').text()
  let telst = $(this).siblings('.telnum').text()
  let dol = $(this).siblings('.Dolznost').text()
  let otd = $(this).siblings('.Otdel').text()
  let mobtel = $(this).siblings('.mobtel').val()
  let kab = $(this).siblings('.kabper').val()


  $("#offcanvasBottomLabel").html("<h5>" + fio +"</h5>")
  $("#photo").attr("src",photo.attr("src"))
  $("#mailadr").html("<h5>" + mail +"</h5>")
  $("#telst").html("<h5>" + telst +"</h5>")
  $("#dolz").html("<h5>" + dol +"</h5>")
  $("#otd").html("<h5>" + otd +"</h5>")
  $("#mobtel").html("<h5>" + mobtel +"</h5>")
  $("#kab").html("<h5>" + kab +"</h5>")
})

$(".textsearch").on('click',function(){
      a = $(this).html()

      $.each($("#table1 tbody tr"), function() {
          if($(this).text().toLowerCase().indexOf((a).toLowerCase()) === -1)
             $(this).hide();
          else
             $(this).show();
      });
    });
