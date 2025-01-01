//SECCION PARA GESTIONAR EL INGRESO A LAS PAGINAS DEL MENU
$(document).ready(function() {
    $('#menu_principal a').on('click', function() {
    var menu = $(this).attr('id');
    seleccion_menu(menu);
    });
});

      function seleccion_menu(menu) {
        switch(menu) {
            case 'creacion_bitacora':
                mostrar_creacion_bitacora();
            break;
            case 'gestion_usuarios':
                mostrar_gestion_usuarios();
            break;
            case 'cargue_planos':
                mostrar_cargue_planos();
            break;
          default:
            console.log('Acción no definida' + menu);
        }
      }


//FUNCION PARA QUE UN USUARIO PUEDA ACCEDER A LA APLICACION
function acceso_usuarios_login(){
    console.log("Ingresando para realizar el logeo del usuario");
    var user=document.getElementById("Username").value;
    var pass=document.getElementById("Password").value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    var data_stringify=JSON.stringify({ usuario: user, password: pass})
    console.log(data_stringify);
    $.ajax({
  type: "POST",
  url: "http://localhost:8000/procesosapp/login_procesos",
  data: data_stringify,
  headers: {'X-CSRFToken': csrfToken},
  mode: 'same-origin',
  contentType: 'application/json',
  success: function(datos){
    console.log("Aqui retorna los datos si el logeo es exitoso")
    console.log(datos);
  },
  dataType: "json"
});
}
// Realizar solicitud AJAX para mostrar la creacion de la bitacora
      function mostrar_creacion_bitacora() {
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        $.ajax({
            url: "http://localhost:8000/calidad/mostrar_creacion_bitacora",
            type: 'GET',
            headers: {'X-CSRFToken': csrfToken},
            mode: 'same-origin',
            success: function(data) {
                $('#mostrar_contenido').html(data);
            },
            error: function(error) {
                console.log("Error:", error);
            }
        });
      }
// Realizar solicitud AJAX para mostrar la gestion de los usuarios
      function mostrar_gestion_usuarios() { 
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        $.ajax({
            url: "http://localhost:8000/calidad/mostrar_gestion_usuarios",
            type: 'GET',
            headers: {'X-CSRFToken': csrfToken},
            mode: 'same-origin',
            success: function(data) {
                $('#mostrar_contenido').html(data);
                mostrar_datatable(data);
            },
            error: function(error) {
                console.log("Error:", error);
            }
        });
 
      }
function mostrar_datatable(data){
    //Creacion del DATATABLE
    const dataSet = [
    ['Tiger Nixon', 'System Architect', 'Edinburgh', '5421', '2011/04/25', '$320,800'],
    ['Garrett Winters', 'Accountant', 'Tokyo', '8422', '2011/07/25', '$170,750'],
    ['Ashton Cox', 'Junior Technical Author', 'San Francisco', '1562', '2009/01/12', '$86,000'],
    ['Cedric Kelly', 'Senior Javascript Developer', 'Edinburgh', '6224', '2012/03/29', '$433,060'],
    ['Airi Satou', 'Accountant', 'Tokyo', '5407', '2008/11/28', '$162,700']];
    new DataTable('#usuarios', {
    columns: [
        { title: 'Name' },
        { title: 'Position' },
        { title: 'Office' },
        { title: 'Extn.' },
        { title: 'Start date' },
        { title: 'Salary' }
    ],
    data: dataSet,
    columnDefs: [
    {
        data: null,
        defaultContent: '<button>Click!</button>',
        targets: -1
    }
    ]
    });
    table.on('click', 'button', function (e) {
        let data = table.row(e.target.closest('tr')).data();
        alert(data[0] + "'s salary is: " + data[5]);
    });
}
// Realizar solicitud AJAX para mostrar el cargue de planos
      function mostrar_cargue_planos() { 
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        $.ajax({
            url: "http://localhost:8000/calidad/mostrar_cargue_planos",
            type: 'GET',
            headers: {'X-CSRFToken': csrfToken},
            mode: 'same-origin',
            success: function(data) {
                $('#mostrar_contenido').html(data);
            },
            error: function(error) {
                console.log("Error:", error);
            }
        });
 
      }