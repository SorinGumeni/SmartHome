var ip = 'broker.hivemq.com';
var port = "8000";
var usessl = true;
var id = (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
var username = '';
var password = '';
var message, client;
var topic;

function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
        console.log("onConnectionLost:" + responseObject.errorMessage);
    }
}

function on_connect(client, userdata, flags, rc)
{
  if(rc==0)
  {
    client.connected_flag=true;
    console.log("connected ok");
  }
  else
  {
    print("Bad connection return code rc="+rc);
    client.bad_connection_flag=true;
  }
}

function connectMQTT() {

    console.log("Connecting to server");
    client = new Paho.MQTT.Client(ip, Number(port), "Client1");
    client.onConnectionLost = onConnectionLost;
    client.on_connect=on_connect;
    client.connect({
        userName: username,
        password: password,
        //useSSL: usessl, dont use it does not connect to the server
        onSuccess: onConnect,
        onFailure: onFailure
    });
}

function onFailure(responseObject) 
{
  console.log("onFailure errorCode/errorMessage: " + responseObject.errorCode + "/" + responseObject.errorMessage);
}

function onConnect() 
{
    console.log("Connected to server");
    message = new Paho.MQTT.Message(message);
    message.destinationName = topic;
    client.send(message);
    client.disconnect();
  }
function GetColorCode(elementID)
{
    var element = document.getElementById(elementID);
    var style;
    window.getComputedStyle;
    style = window.getComputedStyle(element);
    return style.backgroundColor;
}

function ChangeColor(flag)
{
    var colorCode = GetColorCode(flag);

    var green = "rgb(50, 205, 50)";
    var red   = "rgb(220, 20, 60)";
    var grey  = "rgb(128, 128, 128)";
 
    switch (flag)
    {
        case "oLightActive" :
        if(colorCode == "rgb(50, 205, 50)")
        {
          topic = "outside/light";
          message = "ON";
          connectMQTT();
          document.getElementById("oLightActive").style.backgroundColor = red;
          document.getElementById("oLightActive").textContent = "OFF";
          document.getElementById("oLightAutomat").style.backgroundColor = grey;
          document.getElementById("oLightAutomat").style.opacity =  0.6;
          document.getElementById("oLightActive").style.opacity = 1;
        }
        else
        {
          topic = "outside/light";
          message = "OFF";
          connectMQTT();
          document.getElementById("oLightActive").style.backgroundColor = green;
          document.getElementById("oLightActive").textContent = "ON";
          document.getElementById("oLightAutomat").style.opacity =  0.6;
          document.getElementById("oLightActive").style.opacity = 1;
        }
        break;

        case "oLightAutomat" :
        if(colorCode == "rgb(128, 128, 128)")
        {
          topic = "outside/light";
          message = "AUTO";
          connectMQTT();
          document.getElementById("oLightAutomat").style.backgroundColor = "orange";
          document.getElementById("oLightActive").style.backgroundColor = green;
          document.getElementById("oLightActive").textContent = "ON";
          document.getElementById("oLightAutomat").style.opacity = 1;
          document.getElementById("oLightActive").style.opacity =  0.6;
        }
        else
        {
          topic = "outside/light";
          message = "OFF";
          connectMQTT();
          document.getElementById("oLightAutomat").style.backgroundColor = grey;
          document.getElementById("oLightAutomat").style.opacity =  0.6;
          document.getElementById("oLightActive").style.opacity = 1;
        }
        break;

        case "oSecurity" :
        if(colorCode == "rgb(50, 205, 50)")
        {
          document.getElementById("oSecurity").style.backgroundColor = red;
          document.getElementById("oSecurity").textContent = "OFF";
          topic = "outside/security";
          message = "ON";
          connectMQTT();
        }
        else
        {
          document.getElementById("oSecurity").style.backgroundColor = green;
          document.getElementById("oSecurity").textContent = "ON";
          topic = "outside/security";
          message = "OFF";
          connectMQTT();
        }
        break;
        case "oScreenshot":
        {
          topic = "outside/screenshot";
          message = "ON";
          connectMQTT();
        }
        break;

        case "iLightActive" :
        if(colorCode == "rgb(50, 205, 50)")
        {
          topic = "inside/light";
          message = "ON";
          connectMQTT();
          document.getElementById("iLightActive").style.backgroundColor = red;
          document.getElementById("iLightActive").textContent = "OFF";
          document.getElementById("iLightAutomat").style.backgroundColor = grey;
          document.getElementById("iLightAutomat").style.opacity =  0.6;
          document.getElementById("iLightActive").style.opacity = 1;
        }
        else
        {
          topic = "inside/light";
          message = "OFF";
          connectMQTT();
          document.getElementById("iLightActive").style.backgroundColor = green;
          document.getElementById("iLightActive").textContent = "ON";
          document.getElementById("iLightAutomat").style.opacity =  0.6;
          document.getElementById("iLightActive").style.opacity = 1;
        }
        break;

        case "iLightAutomat" :
        if(colorCode == "rgb(128, 128, 128)")
        {
          topic = "inside/light";
          message = "AUTO";
          connectMQTT();
          document.getElementById("iLightAutomat").style.backgroundColor = "orange";
          document.getElementById("iLightActive").style.backgroundColor = green;
          document.getElementById("iLightActive").textContent = "ON";
          document.getElementById("iLightAutomat").style.opacity = 1;
          document.getElementById("iLightActive").style.opacity =  0.6;
        }
        else
        {
          topic = "inside/light";
          message = "OFF";
          connectMQTT();
          document.getElementById("iLightAutomat").style.backgroundColor = grey;
          document.getElementById("iLightAutomat").style.opacity =  0.6;
          document.getElementById("iLightActive").style.opacity = 1;
        }
        break;

        case "iHeating":
        {
          if (colorCode == "rgb(128, 128, 128)")
          {
          topic = "inside/thermostat";
          message = "COOL";
          connectMQTT();
          document.getElementById("iHeating").style.backgroundColor = red;
          document.getElementById("iHeating").style.opacity = 1;
          document.getElementById("iCooling").style.backgroundColor = grey;
          document.getElementById("iCooling").style.opacity = 0.6;
          }
        }
        break;

        case "iCooling":
        {
          if (colorCode == "rgb(128, 128, 128)")
         {
            topic = "inside/thermostat";
            message = "HEAT";
            connectMQTT();
            document.getElementById("iCooling").style.backgroundColor = "blue";
            document.getElementById("iCooling").style.opacity = 1;
            document.getElementById("iHeating").style.backgroundColor = grey;
            document.getElementById("iHeating").style.opacity = 0.6;
          }
        }
        break;
    }
}



function wcqib_refresh_quantity_increments() 
{
    jQuery("div.quantity:not(.buttons_added), td.quantity:not(.buttons_added)").each(function(a, b) {
        var c = jQuery(b);
        c.addClass("buttons_added"), c.children().first().before('<input type="button" value="-" class="minus" />'), c.children().last().after('<input type="button" value="+" class="plus" />')
    })
    console.log("Increment");
}
String.prototype.getDecimals || (String.prototype.getDecimals = function() {
    var a = this,
        b = ("" + a).match(/(?:\.(\d+))?(?:[eE]([+-]?\d+))?$/);
    return b ? Math.max(0, (b[1] ? b[1].length : 0) - (b[2] ? +b[2] : 0)) : 0
}), jQuery(document).ready(function() {
    wcqib_refresh_quantity_increments()
}), jQuery(document).on("updated_wc_div", function() {
    wcqib_refresh_quantity_increments()
}), jQuery(document).on("click", ".plus, .minus", function() {
    var a = jQuery(this).closest(".quantity").find(".qty"),
        b = parseFloat(a.val()),
        c = parseFloat(a.attr("max")),
        d = parseFloat(a.attr("min")),
        e = a.attr("step");
        
    b && "" !== b && "NaN" !== b || (b = 0), "" !== c && "NaN" !== c || (c = ""), "" !== d && "NaN" !== d || 
    (d = 0), "any" !== e && "" !== e && void 0 !== e && "NaN" !== parseFloat(e) || 
    (e = 1), jQuery(this).is(".plus") ? c && b >= c ? a.val(c) : 
    a.val((b + parseFloat(e)).toFixed(e.getDecimals())) : 
    d && b <= d ? a.val(d) : 
    b > 0 && a.val((b - parseFloat(e)).toFixed(e.getDecimals())), a.trigger("change")
});