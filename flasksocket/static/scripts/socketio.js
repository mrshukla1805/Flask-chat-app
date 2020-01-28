document.addEventListener('DOMContentLoaded',() => {
    var socket = io();

    let room = 'Lounge';
    joinRoom("Lounge");

    socket.on('message', data => {

      if(data.username){
        const p = document.createElement('p');
        const span_username =  document.createElement('span');
        const span_timestamp = document.createElement('span');
        const br = document.createElement('br');
        span_username.innerHTML = data.username;
        span_timestamp.innerHTML = data.time_stamp
        p.innerHTML = span_username.outerHTML + br.outerHTML + data.msg
          +br.outerHTML + span_timestamp.outerHTML;
        document.querySelector('#display-message-section').append(p);
      } else {
        printSysMsg(data.msg);
      }
        
    });
 
  

    document.querySelector('#send_message').onclick = () => {
      socket.send({'msg': document.querySelector('#user_message').value,
      'username': username, 'room': room });

      document.querySelector('#user_message').value = '';
    }

    document.querySelectorAll('.select-room').forEach(p =>{
      p.onclick = () =>{
        let newRoom = p.innerHTML;
        if(newRoom == room){
          msg = `You are already in ${room} room.`
          printSysMsg(msg);
        } else{
          leaveRoom(room);
          joinRoom(newRoom);
          room = newRoom;
        }
      }
    });

    function leaveRoom(room) {
      socket.emit('leave', {'username': username ,'room':room});
    }

    function joinRoom(room){
      socket.emit('join', {'username':username, 'room':room});

      document.querySelector('#display-message-section').innerHTML = ''
    
    }

    function printSysMsg(msg) {
      const p = document.createElement('p')
      p.innerHTML = msg;
      document.querySelector('#display-message-section').append(p);
    }

    // Enter message
    let msg = document.querySelector('#user_message');
    msg.addEventListener('keyup', event => {
      event.preventDefault();
      if(event.keyCode === 13){
        document.querySelector('#send_message').click();
      }
    })

});


