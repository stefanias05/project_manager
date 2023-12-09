//Modal de detail task
var detailTaskLinks = document.querySelectorAll('.detailtasklink'); //imi citesc link-urile de detail task in variabila

//iterez fiecare linie si activez eventul de click pt modal
detailTaskLinks.forEach(
    function (link) {
        link.addEventListener('click', function (e) {
            e.preventDefault(); //opresc redirectionarea implicita a link-ului
            var modalId = link.getAttribute('data-target'); //imi citesc id-ul modalului care e acelasi cu data-target din link
            var modal = document.querySelector(modalId); //imi citesc modalul
            if (modal) {
                $(modal).modal("show");
            }
        });
    });


//Modal delete-task
var deleteTaskLinks = document.querySelectorAll('.deletetasklink');
deleteTaskLinks.forEach(
    function (link) {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            var modalID = link.getAttribute('data-target');
            var modal = document.querySelector(modalID);
            if (modal) {
                $(modal).modal("show");
            }
        });
    });


//Modal delete=project

var deleteProjectLinks = document.querySelectorAll('.deleteprojectlink');

deleteProjectLinks.forEach(
    function (link) {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            var modalId = link.getAttribute('data-target');
            var modal = document.querySelector(modalId)
            if (modal) {
                $(modal).modal("show");
            }
        });
    });

//Modal view-notifications
// document.getElementById('allnotifications').addEventListener('click', function (){
//     fetch('/notifications/')
//         .then(response=> response.text())
//         .then(data=>{document.getElementById('notifications').style.display="block";
//             document.getElementById('list-notifications').textContent = data;
//         });
// });
document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('allnotifications').addEventListener('click', function() {
        var myModal = new bootstrap.Modal(document.getElementById('notifications'), {});
        myModal.show();
    });
});