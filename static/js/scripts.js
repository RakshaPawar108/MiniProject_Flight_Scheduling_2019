
function signup(link) {
    let passwd, cpasswd;
    if(!link.localeCompare('/ursignup')){
        passwd = document.getElementById("person-Password").value;
        cpasswd = document.getElementById("person-confirmPass").value;
    }

    if(!passwd.localeCompare(cpasswd)) {
        var n = passwd.length;
        if (n < 8) {
            alert("Password should be more than 8 characters");
            return false;
        }
        else{
            if(!link.localeCompare('/ursignup')) {
                $.ajax({
                    url: '/ursignup' ,
                    type: 'post',
                    data: {
                        person_fname:
                        $('input[name="person-fname"]').val(),
                        person_lname:
                        $('input[name="person-lname"]').val(),
                        person_username:
                        $('input[name="person-username"]').val(),
                        person_Email:
                        $('input[name="person-Email"]').val(),
                        person_Password:
                        $('input[name="person-Password"]').val(),
                        person_Phone:
                        $('input[name="person-Phone"]').val(),
                        person_Address:
                        $('input[name="person-Address"]').val(),
                        person_City:
                        $('input[name="person-City"]').val(),
                        person_State:
                        $('input[name="person-State"]').val(),
                        person_Country:
                        $('input[name="person-Country"]').val(),
                        person_seqQues:
                        $('input[name="person-SeqQues"]').val(),
                        person_seqAns:
                        $('input[name="person-SeqAns"]').val(),
                    },
                    success: function(data) {
                        if(!data.status) {
                            return false;
                        }
                        else {
                            alert("Account Created. Please Log In to Book your Flights");
                            return true;
                            // document.getElementById("firstClassForm").reset();
                        }
                    }
                });
            }
            return false;
        }
    }
    else{
        alert("Both Passwords Don't Match");
        return false;
    }
}

// function search() {
//     var ser = document.getElementById("searching").value;
//     alert(ser)
//
//     $.ajax({
//         url: '/search',
//         type: 'POST',
//         data: {
//             serfli = ser
//         },
//         success: function(data){
//             if(!data.status){
//                 return false;
//             }
//             else {
//                 alert("Search Complete!!!")
//                 document.getElementById("searchresult").innerHTML=data.text;
//                 return true;
//             }
//         }
//
//     });
// }



function login() {
    var uname = document.getElementById("username").value;
    var pass = document.getElementById("pwd").value;
    var n = pass.length;
    alert(uname)

    if(n < 8) {
        alert("Password should be more than 8 characters");
        return false;
    }
    else {
        $.ajax({
            url: '/checkLogin',
            type: 'post',
            data: {
                u_name: uname,
                pass_wd: pass
            },
            success: function(data) {
                if(data.status){
                    window.location = "/profile";
                    return true;
                }
                else {
                    document.getElementById("alert_message").innerHTML=data.text;
                }
            }
        });
    }
}

function boook(){
    var plane = document.getElementById("lol").value;
    alert(plane)

    $.ajax({
        url: '/booked',
        type: 'post',
        data: {
            vimaan: plane
        },
        success: function(data) {
            if(!data.status){
                return false;
            }
            else{
                alert("The flight has been booked!!!!");
                return true;
            }
        }
    });
}
