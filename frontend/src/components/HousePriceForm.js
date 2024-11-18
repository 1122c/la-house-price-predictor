import React, { useState } from 'react';
import axios from 'axios';

const HousePriceForm = () => {
    const [formData, setFormData] = useState({
        GrLivArea: '',
        TotalBsmtSF: '',
        OverallQual: '',
        YearBuilt: '',
        LotArea: '',
    });


    const [prediction, SetPrediction] = useState(null);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault ();
        try {
            const response = await.axios.post();
            SetPrediction(response.data.predicted_price);
        } catch (error) {
            console.error('error making prediction', error);
        }
    };

    return (
        <div></div>
    )
}