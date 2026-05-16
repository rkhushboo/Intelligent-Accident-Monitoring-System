# 📋 QUICK START GUIDE

Get the Customer Retention Intelligence System up and running in 5 minutes!

## ⚡ Super Quick Start (Easiest)

### Windows Users
```bash
cd streamlit_app
run_app.bat
```

### Mac/Linux Users
```bash
cd streamlit_app
chmod +x run_app.sh
./run_app.sh
```

**That's it!** Your app opens at http://localhost:8501

---

## 🔧 Manual Setup (If scripts don't work)

### 1. Open Terminal/Command Prompt

Navigate to project folder:
```bash
cd path\to\streamlit_app
```

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- Streamlit
- Pandas & NumPy
- Scikit-Learn
- LightGBM & XGBoost
- TensorFlow & Keras
- Plotly
- And more...

### 4. Run Application

```bash
streamlit run app.py
```

### 5. Open Browser

Visit: **http://localhost:8501**

---

## 🎯 Using the Application

### First Time

1. **Home Page** - Overview of the system
2. **About Dataset** - Understand the data
3. **EDA & Insights** - Explore patterns
4. **Model Analysis** - Learn about AI models

### Run Predictions

1. Go to **Churn Prediction** page
2. Enter customer details
3. Click "Predict Churn"
4. Review results and recommendations

### Explore Insights

1. Check **Model Comparison** for best model
2. Review **Business Insights** for strategies
3. View **ML Model Analysis** for details

---

## 📊 Application Pages

| Page | Purpose |
|------|---------|
| 🏠 Home | Overview & key metrics |
| 📊 Dataset | Data information |
| 📈 EDA | Data visualization |
| 🤖 ML Model | LightGBM analysis |
| 🧠 ANN Model | Neural network details |
| ⚖️ Comparison | Compare all models |
| 🎯 Prediction | Get churn predictions |
| 💡 Insights | Business recommendations |
| ℹ️ About | Project information |

---

## 🎮 Example Prediction

### Try This Customer:

- **Credit Score**: 600
- **Age**: 50
- **Tenure**: 2 years
- **Balance**: $0
- **Products**: 1
- **Active Member**: No
- **Gender**: Male
- **Geography**: Germany
- **Salary**: $50,000

**Expected Result**: 🔴 HIGH RISK (70%+ churn probability)

---

## ❌ Troubleshooting

### Problem: "Python not found"
**Solution**: Install Python 3.8+ from python.org

### Problem: Port 8501 already in use
**Solution**: Run on different port:
```bash
streamlit run app.py --server.port 8502
```

### Problem: Module not found error
**Solution**: Reinstall dependencies:
```bash
pip install --upgrade -r requirements.txt
```

### Problem: Model loading error
**Solution**: Models use mock data for demo. Errors won't prevent app from running.

### Problem: Slow performance
**Solution**: 
- Reduce data size
- Close other applications
- Increase RAM
- Use GPU for ANN

---

## 📱 Access from Other Devices

### Same Network
```
http://<your-computer-ip>:8501
```

Find your IP:
- **Windows**: Open Command Prompt, run `ipconfig`, find IPv4 Address
- **Mac/Linux**: Open Terminal, run `hostname -I`

### From Internet (Ngrok)
```bash
pip install ngrok
ngrok http 8501
```

Then use the provided URL.

---

## 🚀 Next Steps

After running locally:

1. **Deploy to Cloud**
   - Use Streamlit Cloud (easiest)
   - AWS EC2
   - Docker container
   - See DEPLOYMENT.md

2. **Customize**
   - Add your own data
   - Train models
   - Modify UI
   - Add features

3. **Integrate**
   - Connect to database
   - Add authentication
   - Set up monitoring
   - Implement notifications

4. **Share**
   - Deploy publicly
   - Share with team
   - Showcase to stakeholders
   - Get feedback

---

## 📚 Learn More

- **Full Docs**: See README.md
- **Deployment**: See DEPLOYMENT.md
- **Code**: Explore utils/ and pages/ folders
- **Streamlit Docs**: https://docs.streamlit.io/
- **Machine Learning**: https://scikit-learn.org/
- **Deep Learning**: https://www.tensorflow.org/

---

## 🎓 Project Structure

```
streamlit_app/
├── app.py              ← Main file
├── pages/              ← Different pages
├── utils/              ← Helper functions
├── models/             ← AI models
├── requirements.txt    ← Dependencies
├── README.md           ← Full documentation
├── DEPLOYMENT.md       ← How to deploy
└── QUICKSTART.md       ← This file
```

---

## ✅ Checklist

Before sharing with others:

- [ ] App runs without errors
- [ ] All pages load
- [ ] Predictions work
- [ ] Models load
- [ ] Charts display
- [ ] Mobile-friendly
- [ ] Fast performance
- [ ] Documentation clear

---

## 🆘 Need Help?

1. Check Troubleshooting section above
2. Read error messages carefully
3. Check browser console (F12)
4. Review terminal output
5. Check README.md
6. Search online for error message

---

## 🎉 Success!

Your application is ready to:
- ✅ Predict customer churn
- ✅ Analyze models
- ✅ Explore data
- ✅ Make business decisions

**Start exploring now!** 🚀

---

**Last Updated**: January 2024
**Time to Deploy**: ~5 minutes
**Difficulty**: ⭐ Easy
