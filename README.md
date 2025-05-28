# BlockBoss Marketing Landing Page

A Flask-based landing page for BlockBoss with HTMX and Alpine.js integration, designed for easy Calendly integration with email prefilling.

## Features

- **Responsive Design**: Matches your Visily.ai design with your exact color palette
- **HTMX Integration**: For seamless form submissions and modal loading
- **Alpine.js**: For reactive UI components and state management
- **Calendly Integration Ready**: Supports email prefilling and custom parameters
- **Two-Column Modal**: Professional layout with benefits on left, Calendly on right
- **Email Capture**: Hero form captures emails and passes them to scheduling modal

## Project Structure

```
blockboss_mktg/
├── app.py                 # Flask application with HTMX endpoints
├── requirements.txt       # Python dependencies
├── templates/
│   ├── base.html         # Base template with HTMX/Alpine scripts
│   ├── index.html        # Main landing page
│   ├── about.html        # About page
│   ├── feedback.html     # Feedback page
│   └── contact.html      # Contact page
├── static/
│   ├── css/
│   │   └── style.css     # Complete styling based on your design
│   ├── js/
│   │   └── main.js       # Minimal JS (most functionality in HTMX/Alpine)
│   └── images/           # Logo and partner images (you'll need to add these)
└── README.md
```

## Setup Instructions

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

The app will run at `http://localhost:5000`

### 4. Add Your Images

Add these images to `static/images/`:
- `blockboss-logo.png` - Main logo for navigation
- `blockboss-logo-small.png` - Smaller logo for footer
- `partner-1.png` through `partner-5.png` - Partner/integration logos

### 5. Calendly Integration

To enable Calendly integration:

1. **Get your Calendly URL**: 
   - Go to your Calendly dashboard
   - Copy your meeting link (e.g., `https://calendly.com/yourname/20min-call`)

2. **Update the Flask app**:
   - In `app.py`, line 32, replace `"https://calendly.com/your-calendly-url/20min-advisory-call"` with your actual URL

3. **Enable the Calendly script**:
   - In `templates/base.html`, uncomment line 44:
   ```html
   <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js"></script>
   ```

4. **Remove the placeholder**:
   - In `app.py`, delete or hide the `calendly-temp` div section (lines 70-90 in the modal_html)

## How It Works

### Email Capture Flow

1. **User enters email** in hero form
2. **Form submits via HTMX** to `/api/signup`
3. **Success message shows** with "Schedule your call now" button
4. **Button click opens modal** with email prefilled in Calendly

### Calendly URL Parameters

The system automatically builds Calendly URLs with prefilled data:

```
https://calendly.com/yourname/call?prefill_email=user@example.com
```

You can add more prefill parameters in `app.py`:

```python
# Add these to the calendly_params list:
calendly_params.append("prefill_name=John%20Doe")
calendly_params.append("prefill_custom_1=BlockBoss%20Advisory")
```

### HTMX Endpoints

- `POST /api/signup` - Handles email signups
- `GET /api/advisory-form` - Returns modal HTML with Calendly embed
- `POST /api/advisory-submit` - Handles form submissions (if needed)

### Alpine.js Components

- **emailSignup()**: Handles form validation and state
- **Global notification system**: For toast messages
- **Intersection animations**: For scroll-triggered animations

## Customization

### Color Palette

Colors are defined as CSS variables in `static/css/style.css`:

```css
:root {
    --primary-blue: #005B9F;
    --secondary-green: #28A745;
    --secondary-orange: #F78E1E;
    --neutral-dark: #333333;
    --neutral-mid: #888888;
    --neutral-light: #F5F5F5;
}
```

### Modal Content

Edit the benefits and testimonial in `app.py` within the `api_advisory_form()` function.

### Form Fields

Add custom Calendly form fields by updating the `calendly_params` list in `app.py`.

## Development Notes

### Why HTMX + Alpine.js?

- **HTMX**: Handles server communication without JavaScript
- **Alpine.js**: Provides reactive UI without heavy framework overhead
- **Minimal JS**: Only 20 lines of vanilla JavaScript needed
- **SEO Friendly**: Server-rendered HTML with progressive enhancement

### Future Enhancements

- Add database integration for email storage
- Implement email marketing automation
- Add analytics tracking
- Create admin dashboard for lead management

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile responsive design
- Progressive enhancement (works without JavaScript)

## Deployment

Ready for deployment to:
- Heroku
- Vercel
- Railway
- Any Python hosting service

Just ensure `Flask` and `Werkzeug` are installed in your production environment. 