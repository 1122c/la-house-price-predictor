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
        <div>
            <h2>House Price Prediction</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    GrLivArea:
                    <input
                    type="number"
                    name="GrLivArea"
                    value={formData.GrLivArea}
                    onChange={handleChange}
                    />
                </label>
                <br />
                <label>
                    TotalBsmtSF:
                    <input
                    type="number"
                    name="TotalBsmtSF"
                    value={formData.TotalBsmtSF}
                    onChange={handleChange}
                    />
                </label>
                <br />
                <label>
                    OverallQual:
                    <input
                    type="number"
                    name="OverallQual"
                    value={formData.OverallQual}
                    onChange={handleChange}
                    />
                </label>
                <br />
                <label>
                    YearBuilt:
                    <input>
                    type="number"
                    name="YearBuilt"
                    value={formData.YearBuilt}
                    onChange{handleChange}
                    </input>
                </label>
                <br />
                <label>
                    LotArea:
                    <input
                    type="number"
                    name="LotArea"
                    value={formData.LotArea}
                    onChange={handleChange}
                    />
                </label>
                <br />
                <button type="submit">Predict Price</button>
            </form>
            {prediction !== null &&(
                <div>
                    <h3>Predicted Price: ${prediction}</h3>
                    </div>
            )}
        </div>
    );
};

export default HousePriceForm;