$(document).ready(()=>{
    $("form[name=signup]").submit((eve)=>{
        eve.preventDefault()
        $("#errUname").hide()
        $("#errPass").hide()

        var Uname=$("input[name=Uname]").val()
        var pass=$("input[name=pass]").val()
        var valid=true

        // form validation
        if(Uname.length==0){
            $("#errUname").html("<br/>FirstName shouldn't empty")
            $("#errUname").show()
            valid=false
        }
        if(pass.length==0){
            $("#errPass").html("<br/>Password shouldn't empty")
            $("#errPass").show()
            valid=false
        }

        // data validation
        if(!("Sadhasivam").test(Uname)){
            $("#errUname").html("<br/>*User Name Mismatch")
            $("#errUname").show()
            valid=false
        }
        if(!("srikalpana12@").test(Uname)){
            $("#errPass").html("<br/>*Password Mismatch")
            $("#errPass").show()
            valid=false
        }
        if(user=="Sadhasivam"&&pass=="srikalpana12@")
        {
            $("#enter").dblclick(()=>{
                $(location).prop("href","/frames.html")
            })
         }
        
        return valid

    })
})