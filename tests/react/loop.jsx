import React, { Component } from 'react'

function loop() {
    let nb = [1, 2, 3]

    return (
        <div>
            {nb.map((e) => test.map((x) => <Component number={x}/>))}
        </div>
    )
    
}