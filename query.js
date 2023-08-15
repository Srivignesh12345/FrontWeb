$(document).ready(()=>{
    $("form[name=signup]").submit((eve)=>{
        eve.preventDefault()
        $("#errFname").hide()
        $("#errPemail").hide()
        $("#errMob").hide()
        $("#erraddress").hide()
        
        var fname=$("input[name=firstName]").val()
        var pri=$("input[name=primary]").val()
        var mob=$("input[name=mobile]").val()
        var address=$("input[name=address]").val()
        var valid=true

        // form validation
        if(fname.length==0){
            $("#errFname").html("<br/>FirstName shouldn't empty")
            $("#errFname").show()
            valid=false
        }
        if(pri.length==0){
            $("#errPemail").html("<br/>Primary email shouldn't empty")
            $("#errPemail").show()
            valid=false
        }
        if(mob.length==0){
            $("#errMob").html("<br/>Mobile number shouldn't empty")
            $("#errMob").show()
            valid=false
        }
        if(address.length==0){
            $("#erraddress").html("<br/>Address shouldn't empty")
        }

        // data validation
        if((/[0-9!@#$%^&*()]/).test(fname)){
            $("#errFname").html("<br/>FirstName shouldn't contains numbers or special characters")
            $("#errFname").show()
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
        return valid

    })
})