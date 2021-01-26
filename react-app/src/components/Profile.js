import React from 'react';

import Hobbies from './Hobbies'

const Profile = () =>
(
    <div>
        <h1>Jason Zhang</h1>
        <h2>Computer Science</h2>
        <h3>Year: Junior</h3>
        <h3>Ideal vacation</h3>
        <img style={{width: 200, height: 150}} src="https://d25tv1xepz39hi.cloudfront.net/2016-05-05/files/6D_Landscape_Gardensbythebay_2.jpg"></img>
        <Hobbies />
    </div>
)

export default Profile;