from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# HTMX API endpoints
@app.route('/api/signup', methods=['POST'])
def api_signup():
    email = request.form.get('email')
    
    if not email:
        return '', 400
    
    # TODO: Add email to database/mailing list
    # For now, just return success
    print(f"New signup: {email}")
    
    return '', 200

@app.route('/api/advisory-form', methods=['GET'])
def api_advisory_form():
    # Get email from query parameters if provided
    email = request.args.get('email', request.form.get('email', ''))
    
    # Calendly URL parameters for prefilling
    # Format: https://calendly.com/your-link?prefill_email=user@example.com&prefill_name=John%20Doe
    calendly_base_url = "https://calendly.com/george_bilbrey/20-minute-meeting"
    calendly_params = []
    
    if email:
        calendly_params.append(f"prefill_email={email}")
    
    # You can add more prefill parameters as needed:
    # calendly_params.append("prefill_name=")
    # calendly_params.append("prefill_custom_1=BlockBoss%20Advisory")
    
    calendly_url = calendly_base_url
    if calendly_params:
        calendly_url += "?" + "&".join(calendly_params)
    
    # Return a two-column modal with text and Calendly embed
    modal_html = f'''
    <div class="modal-content modal-two-column">
        <button class="modal-close" onclick="document.getElementById('advisory-modal').innerHTML=''">&times;</button>
        
        <div class="modal-left">
            <h2>Join Our Advisory Group</h2>
            <p class="modal-subtitle">Shape the future of BlockBoss and get exclusive benefits</p>
            
            <div class="benefit-list">
                <div class="benefit-item">
                    <div class="benefit-icon">▶</div>
                    <div>
                        <h4>Shape the Product</h4>
                        <p>Hold a 20-minute call with our founder to share your insights and challenges</p>
                    </div>
                </div>
                
                <div class="benefit-item">
                    <div class="benefit-icon">▶</div>
                    <div>
                        <h4>Get Free Campaigns</h4>
                        <p>Receive 20 complimentary postcards and QR-linked marketing materials</p>
                    </div>
                </div>
                
                <div class="benefit-item">
                    <div class="benefit-icon">▶</div>
                    <div>
                        <h4>Insider Discounts</h4>
                        <p>Founding members lock in exclusive rates when we launch</p>
                    </div>
                </div>
                
                <div class="benefit-item">
                    <div class="benefit-icon">▶</div>
                    <div>
                        <h4>Early Access</h4>
                        <p>Be the first to test new features and get priority support</p>
                    </div>
                </div>
            </div>
            
            <div class="testimonial">
                <p><em>"BlockBoss helped us generate 40% more leads in our first month. The targeting is incredible!"</em></p>
                <span>- Sarah M., Pest Control Pro</span>
            </div>
            
            {f'<div class="email-confirmation"><strong>Scheduling for:</strong> {email}</div>' if email else ''}
        </div>
        
        <div class="modal-right">
            <div class="calendly-container">
                <h3>Schedule Your Call</h3>
                <p>Pick a time that works for you. No pressure, just a friendly conversation about growing your business.</p>
                
                <!-- Calendly embed will go here -->
                <div class="calendly-embed-container">
                    <div class="calendly-inline-widget" 
                         data-url="{calendly_url}"
                         style="min-width:320px;height:630px;">
                    </div>
                </div>
            </div>
        </div>
    </div>
    '''
    return modal_html

@app.route('/api/advisory-submit', methods=['POST'])
def api_advisory_submit():
    # Process advisory form submission
    name = request.form.get('name')
    email = request.form.get('email')
    company = request.form.get('company')
    challenges = request.form.get('challenges')
    
    # TODO: Save to database
    print(f"Advisory application: {name} ({email}) from {company}")
    
    return '''
    <div class="modal-content">
        <h3>Application Submitted!</h3>
        <p>Thank you for your interest in joining our advisory group. We'll be in touch within 24 hours to schedule your 20-minute call with our founder.</p>
        <button type="button" class="btn btn-orange" onclick="document.getElementById('advisory-modal').innerHTML=''">Close</button>
    </div>
    '''

if __name__ == '__main__':
    app.run(debug=True) 