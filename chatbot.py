import json

def get_response(user_message, college_data):
    msg = user_message.lower().strip()

    # TIMINGS
    if any(w in msg for w in ['timing', 'time', 'schedule', 'hours', 'open', 'close', 'when']):
        t = college_data.get('timings', {})
        return f"""⏰ **VVITU Timings:**

🏫 College: {t.get('college', '8:00 AM - 3:50 PM')}
📚 Library: {t.get('library', '9:00 AM - 4:00 PM')}
🍽️ Canteen: {t.get('canteen', '8:00 AM - 4:00 PM')}
🏢 Office: {t.get('office', '9:00 AM - 5:00 PM')}
📅 Working Days: Monday to Saturday

Is there anything else I can help you with? 😊"""

    # FEES
    elif any(w in msg for w in ['fee', 'fees', 'cost', 'price', 'money', 'pay', 'tuition', 'amount']):
        fees = college_data.get('fees', {})
        return f"""💰 **VVITU Fee Structure (Per Year):**

💻 CSM (AI & ML): ₹{fees.get('CSM', 250000):,}
🖥️ CSE: ₹{fees.get('CSE', 200000):,}
🏗️ Civil Engineering: ₹{fees.get('CIVIL', 150000):,}
⚙️ Mechanical: ₹{fees.get('MECHANICAL', 15000):,}
📡 ECE: ₹{fees.get('ECE', 20000):,}
⚡ EEE: ₹{fees.get('EEE', 150000):,}
💼 BBA: ₹{fees.get('BBA', 200000):,}
🎓 MBA: ₹{fees.get('MBA', 230000):,}
🔐 CIC (IOT & Cyber): ₹{fees.get('CIC', 200000):,}
📊 CAD (AI & Data): ₹{fees.get('CAD', 180000):,}
🤖 CAI (AI): ₹{fees.get('CAI', 200000):,}

📌 Note: Scholarships available for eligible students!

Is there anything else I can help you with? 😊"""

    # HOSTEL
    elif any(w in msg for w in ['hostel', 'accommodation', 'stay', 'room', 'boarding', 'lodge']):
        h = college_data.get('facilities', {})
        return f"""🏠 **VVITU Hostel Facilities:**

✅ Hostel available for both Boys & Girls
💰 Fee: ₹1,00,000 per year (includes food)
🍽️ Mess/Food included in hostel fee
🔒 Secure campus with 24/7 Z+security
📞 Contact: {college_data.get('contact', '09100305336')}

Is there anything else I can help you with? 😊"""

    # DEPARTMENTS
    elif any(w in msg for w in ['department', 'branch', 'course', 'program', 'study', 'field', 'stream']):
        depts = college_data.get('departments', {})
        result = "🏫 **VVITU Departments:**\n\n"
        icons = ['💻', '🖥️', '🏗️', '⚙️', '📡', '⚡', '💼', '🎓', '🔐', '📊', '🤖']
        for i, (code, name) in enumerate(depts.items()):
            icon = icons[i] if i < len(icons) else '📚'
            result += f"{icon} **{code}**: {name}\n"
        result += "\nIs there anything else I can help you with? 😊"
        return result

    # PLACEMENTS
    elif any(w in msg for w in ['placement', 'job', 'company', 'package', 'salary', 'recruit', 'career', 'lpa', 'hire']):
        p = college_data.get('placements', {})
        companies = ', '.join(p.get('top_companies', []))
        return f"""💼 **VVITU Placements:**

📈 Average Package: {p.get('average_package', '6.5 LPA')}
🏆 Highest Package: {p.get('highest_package', '44 LPA')}
✅ Placement Rate: {p.get('placement_rate', '85%')}
👥 Students Placed 2024: {p.get('total_placed_2025', '500+')}

🏢 **Top Recruiting Companies:**
{companies}

🎯 Dedicated Training & Placement Cell available!

Is there anything else I can help you with? 😊"""

    # ACTIVITIES / CLUBS
    elif any(w in msg for w in ['activit', 'club', 'sport', 'event', 'fest', 'extra', 'ncc', 'nss', 'cultural', 'dance', 'music']):
        e = college_data.get('extra_curriculum', {})
        clubs = '\n'.join([f"🎯 {c}" for c in e.get('clubs', [])])
        return f"""🎭 **VVITU Extra Curricular Activities:**

🪖 **NCC**: {e.get('NCC', 'National Cadet Corps training')}
🤝 **NSS**: {e.get('NSS', 'National Service Scheme')}
🎉 **Annual Fest**: {e.get('annual_fest', 'Cultural events and competitions')}
💡 **Tech Fest**: {e.get('tech_fest', 'Hackathons and project expo')}

🎪 **Clubs:**
{clubs}

Is there anything else I can help you with? 😊"""

    # ADMISSION
    elif any(w in msg for w in ['admission', 'apply', 'join', 'enroll', 'eamcet', 'document', 'eligib']):
        a = college_data.get('admission', {})
        docs = '\n'.join([f"📄 {d}" for d in a.get('documents_required', [])])
        return f"""📝 **VVITU Admissions:**

🎯 Process: {a.get('process', 'Through AP EAMCET counseling')}

📋 **Documents Required:**
{docs}

📞 Contact: {a.get('phone', '09100305336')}
📧 Email: {a.get('contact', 'admissions@vvitu.ac.in')}

Is there anything else I can help you with? 😊"""

    # LIBRARY
    elif any(w in msg for w in ['library', 'book', 'read', 'study room']):
        return f"""📚 **VVITU Library:**

⏰ Timing: 8:00 AM - 4:00 PM
📖 Books: 50,000+ books available
💻 Digital resources available
🪑 Spacious reading rooms
📅 Open: Monday to Saturday

Is there anything else I can help you with? 😊"""

    # TRANSPORT / BUS
    elif any(w in msg for w in ['bus', 'transport', 'vehicle', 'travel', 'route']):
        return f"""🚌 **VVITU Transport:**

🕖 Bus Start Time: 7:00 AM
🗺️ Routes: From all major city points
📞 Transport Office: {college_data.get('contact', '09100305336')}

Contact transport office for route details and fees!

Is there anything else I can help you with? 😊"""

    # SCHOLARSHIPS
    elif any(w in msg for w in ['scholarship', 'free', 'discount', 'financial', 'aid', 'concession']):
        s = college_data.get('scholarships', {})
        return f"""🎓 **VVITU Scholarships:**

🏛️ Government: {s.get('government', 'SC/ST/BC scholarships from AP Government')}
⭐ Merit: {s.get('merit', 'For top EAMCET rankers')}
🏆 Sports: Fee concession for state-level sports achievers
📞 Contact: {s.get('contact', '9100 305 336 , 9959 404 336 , 7702 943 336')}

Is there anything else I can help you with? 😊"""

    # CONTACT
    elif any(w in msg for w in ['contact', 'phone', 'number', 'address', 'location', 'where', 'call', 'email', 'website']):
        c = college_data.get('important_contacts', {})
        return f"""📞 **VVITU Contact Details:**

📱 Main Office: {c.get('main_office', '09100305336')}
🌐 Website: {c.get('website', 'www.vvitu.ac.in')}
📧 Email: {c.get('email', 'admissions@vvitu.ac.in')}
📍 Location: Namburu, Guntur, Andhra Pradesh
👨‍💼 Registrar: {college_data.get('registrar', 'Dr. Y Mallikarjuna Reddy')}

Is there anything else I can help you with? 😊"""

    # FACILITIES
    elif any(w in msg for w in ['facilit', 'wifi', 'canteen', 'food', 'pool', 'swimming', 'lab', 'medical', 'auditorium']):
        f = college_data.get('facilities', {})
        return f"""🏛️ **VVITU Facilities:**

📶 WiFi: {f.get('wifi', 'High speed WiFi across campus')}
🍽️ Canteen: {f.get('canteen', 'Affordable food all day')}
🏊 Swimming Pool: {f.get('swimming_pool', 'Available on campus')}
🔬 Labs: {f.get('labs', 'Modern computer and engineering labs')}
🏟️ Auditorium: {f.get('auditorium', 'Large auditorium for events')}
🏥 Medical: {f.get('medical', 'On-campus medical room')}
🚌 Buses: {f.get('buses', 'From major city points at 7 AM')}

Is there anything else I can help you with? 😊"""

    # ABOUT VVITU
    elif any(w in msg for w in ['about', 'vvitu', 'university', 'college', 'history', 'established', 'founded', 'info']):
        return f"""🏛️ **About VVITU:**

🎓 Full Name: {college_data.get('college_name')}
📍 Location: {college_data.get('location')}
📅 Established: {college_data.get('established')}
💬 Motto: "{college_data.get('motto')}"
🌐 Website: {college_data.get('website')}
📞 Contact: {college_data.get('contact')}
👨‍💼 Registrar: {college_data.get('registrar')}
🏫 Type: {college_data.get('type')}

Is there anything else I can help you with? 😊"""

    # ABOUT FM GUIDER
    elif any(w in msg for w in ['who are you', 'fm guider', 'your name', 'created', 'made by', 'developer']):
        return """🤖 **I am FM Guider!**

I'm your personal AI companion for VVITU, created by two passionate students:
👨‍💻 **Fayaz** & **Masthan** — VVITU 2026

I'm here 24/7 to help new students know everything about VVITU!

Is there anything else I can help you with? 😊"""

    # DEFAULT
    else:
        return f"""🤔 I'm not sure about that specific topic!

Here's what I can help you with:
⏰ **Timings** | 💰 **Fees** | 🏠 **Hostel**
🏫 **Departments** | 💼 **Placements** | 🎭 **Activities**
📝 **Admissions** | 📚 **Library** | 🚌 **Transport**
🎓 **Scholarships** | 📞 **Contact** | 🏛️ **About VVITU**

Just ask me anything about VVITU! 😊

For more info contact: {college_data.get('contact', '09100305336')}

Is there anything else I can help you with? 😊"""
