$(document).ready(()=>{
    $("form[name=signup]").submit((eve)=>{
        eve.preventDefault()
        $("#errUser").hide()
        $("#errPass").hide()
        $("#errCpass").hide()
        $("#errMob").hide()
        $("#errProfile").hide()
        $("#errLocation").hide()

        var fname=$("input[name=UserName]").val()
        var pass=$("input[name=choose]").val()
        var con=$("input[name=confirm]").val()
        var mob=$("input[name=mobile]").val()
        //var type=$("input[name=type]:checked")
        var loc=$("select[name=location]").val()

        var valid=true

        // form validation
        if(fname.length==0){
            $("#errUser").html("<br/>FirstName shouldn't empty")
            $("#errUser").show()
            valid=false
        }
        if(pass.length==0){
            $("#errPass").html("<br/>Password shouldn't empty")
            $("#errPass").show()
            valid=false
        }
        if(con.length==0){
            $("#errCpass").html("<br/>Confirm Password shouldn't empty")
            $("#errCpass").show()
            valid=false
        }
        if(mob.length==0){
            $("#errMob").html("<br/>Mobile number shouldn't empty")
            $("#errMob").show()
            valid=false
        }
        if($("input[name=type]:checked").length==0){
            $("#errProfile").html("<br/>Profile type shouldn't empty")
            $("#errProfile").show()
            valid=false
        }
        if(loc=="Select location"){
            $("#errLocation").html("<br/>Location shouldn't empty")
            $("#errLocation").show()
            valid=false
        }

        // data validation
        if((/[0-9!@#$%^&*()]/).test(fname)){
            $("#errUser").html("<br/>FirstName shouldn't contains numbers or special characters")
            $("#errUser").show()
            valid=false
        }
        if((/[0-9!@#$%^&*()]/).test(lname)){
            $("#errLname").html("<br/>LastName shouldn't contains numbers or special characters")
            $("#errLname").show()
            valid=false
        }
        if((/[a-zA-Z]/).test(mob)||(/[0-9]{11}/).test(mob)){
            $("#errMob").html("<br/>Invalid mobile number")
            $("#errMob").show()
            valid=false
        }
        if(pri.indexOf("@")<2||(pri.lastIndexOf(".")-pri.indexOf("@"))<3){
            $("#errPemail").html("<br/>Primary email isn't valid")
            $("#errPemail").show()
            valid=false
        }
        if(alter.indexOf("@")<2||(alter.lastIndexOf(".")-alter.indexOf("@"))<3){
            $("#errSemail").html("<br/>Alternate email isn't valid")
            $("#errSemail").show()
            valid=false
        }
        if(pri==alter){
            $("#errPemail").html("<br/>Primary and Alternate email shouldn't same")
            $("#errSemail").html("<br/>Primary and Alternate email shouldn't same")
            $("#errSemail").show()
            $("#errPemail").show()
            valid=false
        }
        if(!(/(?=.*[0-9])(?=.*[!@#$^])[A-Za-z0-9!@#$^]{8,}/).test(pass)){
            $("#errPass").html("<br/>Invalid password")
            $("#errPass").show()
            valid=false
        }
        if(!(/(?=.*[0-9])(?=.*[!@#$^])[A-Za-z0-9!@#$^]{8,}/).test(con)){
            $("#errCpass").html("<br/>Invalid password")
            $("#errCpass").show()
            valid=false
        }
        if(pass!=con){
            $("#errPass").html("<br/>Password mismatch")
            $("#errCpass").html("<br/>Password mismatch")
            $("#errPass").show()
            $("#errCpass").show()
            valid=false
        }

        return valid

    })
})