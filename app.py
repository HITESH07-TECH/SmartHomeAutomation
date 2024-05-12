from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'dev'  # Replace with your secret key

# Database configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql@HYB0610",
    database="smarthomeautomation"
)

cursor = db.cursor()

app.static_url_path = '/static'

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cursor.execute("SELECT * FROM userauth WHERE UserName=%s AND Password=%s", (username, password))
        user = cursor.fetchone()

        if user:
            session['loggedin'] = True
            session['username'] = user[1]
            return redirect('/dashboard')
        else:
            return render_template('login.html', message="Invalid credentials!")
    else:
        return render_template('login.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/')

# Logout route
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect('/')

# Device CRUD routes
@app.route('/view_devices')
def view_devices():
    cursor.execute("SELECT * FROM Device")
    devices = cursor.fetchall()
    return render_template('view_devices.html', devices=devices)

@app.route('/add_device', methods=['GET', 'POST'])
def add_device():
    if request.method == 'POST':
        # Retrieve form data
        device_name = request.form['device_name']
        device_type = request.form['device_type']
        manufacturer = request.form['manufacturer']
        status = request.form['status']
        
        # Insert data into Device table
        cursor.execute("INSERT INTO Device (DeviceName, DeviceType, Manufacturer, Status) VALUES (%s, %s, %s, %s)", (device_name, device_type, manufacturer, status))
        db.commit()
        return redirect('/view_devices')
    else:
        return render_template('add_device.html')

@app.route('/update_device/<int:device_id>', methods=['GET', 'POST'])
def update_device(device_id):
    if request.method == 'POST':
        # Retrieve form data
        device_name = request.form['device_name']
        device_type = request.form['device_type']
        manufacturer = request.form['manufacturer']
        status = request.form['status']
        
        # Update data in Device table
        cursor.execute("UPDATE Device SET DeviceName=%s, DeviceType=%s, Manufacturer=%s, Status=%s WHERE DeviceID=%s", (device_name, device_type, manufacturer, status, device_id))
        db.commit()
        return redirect('/view_devices')
    else:
        cursor.execute("SELECT * FROM Device WHERE DeviceID=%s", (device_id,))
        device = cursor.fetchone()
        return render_template('update_device.html', device=device)

@app.route('/delete_device/<int:device_id>')
def delete_device(device_id):
    cursor.execute("DELETE FROM Device WHERE DeviceID=%s", (device_id,))
    db.commit()
    return redirect('/view_devices')

# User CRUD Routes
@app.route('/view_users')
def view_users():
    cursor.execute("SELECT * FROM User")
    users = cursor.fetchall()
    return render_template('view_users.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        contact_number = request.form['contact_number']
        user_type = request.form['user_type']
        
        # Insert data into User table
        cursor.execute("INSERT INTO User (UserName, Password, Email, ContactNumber, UserType) VALUES (%s, %s, %s, %s, %s)", (username, password, email, contact_number, user_type))
        db.commit()
        return redirect('/view_users')
    else:
        return render_template('add_user.html')

@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    if request.method == 'POST':
        # Retrieve form data
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        contact_number = request.form['contact_number']
        user_type = request.form['user_type']
        
        # Update data in User table
        cursor.execute("UPDATE User SET UserName=%s, Password=%s, Email=%s, ContactNumber=%s, UserType=%s WHERE UserID=%s", (username, password, email, contact_number, user_type, user_id))
        db.commit()
        return redirect('/view_users')
    else:
        cursor.execute("SELECT * FROM User WHERE UserID=%s", (user_id,))
        user = cursor.fetchone()
        return render_template('update_user.html', user=user)

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    cursor.execute("DELETE FROM User WHERE UserID=%s", (user_id,))
    db.commit()
    return redirect('/view_users')

#AutomationScenario CRUD Routes
@app.route('/view_automation_scenarios')
def view_automation_scenarios():
    cursor.execute("SELECT * FROM AutomationScenario")
    automation_scenarios = cursor.fetchall()
    return render_template('view_automation_scenarios.html', automation_scenarios=automation_scenarios)

@app.route('/add_automation_scenario', methods=['GET', 'POST'])
def add_automation_scenario():
    if request.method == 'POST':
        # Retrieve form data
        scenario_name = request.form['scenario_name']
        description = request.form['description']
        activation_condition = request.form['activation_condition']
        actions = request.form['actions']
        
        # Insert data into AutomationScenario table
        cursor.execute("INSERT INTO AutomationScenario (ScenarioName, Description, ActivationCondition, Actions) VALUES (%s, %s, %s, %s)", (scenario_name, description, activation_condition, actions))
        db.commit()
        return redirect('/view_automation_scenarios')
    else:
        return render_template('add_automation_scenario.html')

@app.route('/update_automation_scenario/<int:scenario_id>', methods=['GET', 'POST'])
def update_automation_scenario(scenario_id):
    if request.method == 'POST':
        # Retrieve form data
        scenario_name = request.form['scenario_name']
        description = request.form['description']
        activation_condition = request.form['activation_condition']
        actions = request.form['actions']
        
        # Update data in AutomationScenario table
        cursor.execute("UPDATE AutomationScenario SET ScenarioName=%s, Description=%s, ActivationCondition=%s, Actions=%s WHERE ScenarioID=%s", (scenario_name, description, activation_condition, actions, scenario_id))
        db.commit()
        return redirect('/view_automation_scenarios')
    else:
        cursor.execute("SELECT * FROM AutomationScenario WHERE ScenarioID=%s", (scenario_id,))
        scenario = cursor.fetchone()
        return render_template('update_automation_scenario.html', scenario=scenario)

@app.route('/delete_automation_scenario/<int:scenario_id>')
def delete_automation_scenario(scenario_id):
    cursor.execute("DELETE FROM AutomationScenario WHERE ScenarioID=%s", (scenario_id,))
    db.commit()
    return redirect('/view_automation_scenarios')

#Sensor CRUD Routes
@app.route('/view_sensors')
def view_sensors():
    cursor.execute("SELECT * FROM Sensor")
    sensors = cursor.fetchall()
    return render_template('view_sensors.html', sensors=sensors)

@app.route('/add_sensor', methods=['GET', 'POST'])
def add_sensor():
    if request.method == 'POST':
        # Retrieve form data
        sensor_type = request.form['sensor_type']
        device_id = request.form['device_id']
        sensor_location = request.form['sensor_location']
        current_value = request.form['current_value']
        last_update_date_time = request.form['last_update_date_time']
        
        # Insert data into Sensor table
        cursor.execute("INSERT INTO Sensor (SensorType, DeviceID, SensorLocation, CurrentValue, LastUpdateDateTime) VALUES (%s, %s, %s, %s, %s)", (sensor_type, device_id, sensor_location, current_value, last_update_date_time))
        db.commit()
        return redirect('/view_sensors')
    else:
        return render_template('add_sensor.html')

@app.route('/update_sensor/<int:sensor_id>', methods=['GET', 'POST'])
def update_sensor(sensor_id):
    if request.method == 'POST':
        # Retrieve form data
        sensor_type = request.form['sensor_type']
        device_id = request.form['device_id']
        sensor_location = request.form['sensor_location']
        current_value = request.form['current_value']
        last_update_date_time = request.form['last_update_date_time']
        
        # Update data in Sensor table
        cursor.execute("UPDATE Sensor SET SensorType=%s, DeviceID=%s, SensorLocation=%s, CurrentValue=%s, LastUpdateDateTime=%s WHERE SensorID=%s", (sensor_type, device_id, sensor_location, current_value, last_update_date_time, sensor_id))
        db.commit()
        return redirect('/view_sensors')
    else:
        cursor.execute("SELECT * FROM Sensor WHERE SensorID=%s", (sensor_id,))
        sensor = cursor.fetchone()
        return render_template('update_sensor.html', sensor=sensor)

@app.route('/delete_sensor/<int:sensor_id>')
def delete_sensor(sensor_id):
    cursor.execute("DELETE FROM Sensor WHERE SensorID=%s", (sensor_id,))
    db.commit()
    return redirect('/view_sensors')

#SecuritySystem CRUD Routes
@app.route('/view_security_systems')
def view_security_systems():
    cursor.execute("SELECT * FROM SecuritySystem")
    security_systems = cursor.fetchall()
    return render_template('view_security_systems.html', security_systems=security_systems)

@app.route('/add_security_system', methods=['GET', 'POST'])
def add_security_system():
    if request.method == 'POST':
        # Retrieve form data
        device_ids = request.form['device_ids']
        arm_status = request.form['arm_status']
        security_mode = request.form['security_mode']
        alarm_trigger_conditions = request.form['alarm_trigger_conditions']
        
        # Insert data into SecuritySystem table
        cursor.execute("INSERT INTO SecuritySystem (DeviceIDs, ArmStatus, SecurityMode, AlarmTriggerConditions) VALUES (%s, %s, %s, %s)", (device_ids, arm_status, security_mode, alarm_trigger_conditions))
        db.commit()
        return redirect('/view_security_systems')
    else:
        return render_template('add_security_system.html')

@app.route('/update_security_system/<int:system_id>', methods=['GET', 'POST'])
def update_security_system(system_id):
    if request.method == 'POST':
        # Retrieve form data
        device_ids = request.form['device_ids']
        arm_status = request.form['arm_status']
        security_mode = request.form['security_mode']
        alarm_trigger_conditions = request.form['alarm_trigger_conditions']
        
        # Update data in SecuritySystem table
        cursor.execute("UPDATE SecuritySystem SET DeviceIDs=%s, ArmStatus=%s, SecurityMode=%s, AlarmTriggerConditions=%s WHERE SystemID=%s", (device_ids, arm_status, security_mode, alarm_trigger_conditions, system_id))
        db.commit()
        return redirect('/view_security_systems')
    else:
        cursor.execute("SELECT * FROM SecuritySystem WHERE SystemID=%s", (system_id,))
        system = cursor.fetchone()
        return render_template('update_security_system.html', system=system)

@app.route('/delete_security_system/<int:system_id>')
def delete_security_system(system_id):
    cursor.execute("DELETE FROM SecuritySystem WHERE SystemID=%s", (system_id,))
    db.commit()
    return redirect('/view_security_systems')

#EnergyManagement CRUD Routes
@app.route('/view_energy_managements')
def view_energy_managements():
    cursor.execute("SELECT * FROM EnergyManagement")
    energy_managements = cursor.fetchall()
    return render_template('view_energy_managements.html', energy_managements=energy_managements)

@app.route('/add_energy_management', methods=['GET', 'POST'])
def add_energy_management():
    if request.method == 'POST':
        # Retrieve form data
        device_ids = request.form['device_ids']
        power_usage_threshold = request.form['power_usage_threshold']
        energy_cost_per_unit = request.form['energy_cost_per_unit']
        alerts_threshold = request.form['alerts_threshold']
        
        # Insert data into EnergyManagement table
        cursor.execute("INSERT INTO EnergyManagement (DeviceIDs, PowerUsageThreshold, EnergyCostPerUnit, AlertsThreshold) VALUES (%s, %s, %s, %s)", (device_ids, power_usage_threshold, energy_cost_per_unit, alerts_threshold))
        db.commit()
        return redirect('/view_energy_managements')
    else:
        return render_template('add_energy_management.html')

@app.route('/update_energy_management/<int:management_id>', methods=['GET', 'POST'])
def update_energy_management(management_id):
    if request.method == 'POST':
        # Retrieve form data
        device_ids = request.form['device_ids']
        power_usage_threshold = request.form['power_usage_threshold']
        energy_cost_per_unit = request.form['energy_cost_per_unit']
        alerts_threshold = request.form['alerts_threshold']
        
        # Update data in EnergyManagement table
        cursor.execute("UPDATE EnergyManagement SET DeviceIDs=%s, PowerUsageThreshold=%s, EnergyCostPerUnit=%s, AlertsThreshold=%s WHERE ManagementID=%s", (device_ids, power_usage_threshold, energy_cost_per_unit, alerts_threshold, management_id))
        db.commit()
        return redirect('/view_energy_managements')
    else:
        cursor.execute("SELECT * FROM EnergyManagement WHERE ManagementID=%s", (management_id,))
        management = cursor.fetchone()
        return render_template('update_energy_management.html', management=management)

@app.route('/delete_energy_management/<int:management_id>')
def delete_energy_management(management_id):
    cursor.execute("DELETE FROM EnergyManagement WHERE ManagementID=%s", (management_id,))
    db.commit()
    return redirect('/view_energy_managements')

#NotificationLog CRUD Routes
@app.route('/view_notification_logs')
def view_notification_logs():
    cursor.execute("SELECT * FROM NotificationLog")
    notification_logs = cursor.fetchall()
    return render_template('view_notification_logs.html', notification_logs=notification_logs)

@app.route('/add_notification_log', methods=['GET', 'POST'])
def add_notification_log():
    if request.method == 'POST':
        # Retrieve form data
        user_id = request.form['user_id']
        notification_type = request.form['notification_type']
        notification_content = request.form['notification_content']
        notification_date_time = request.form['notification_date_time']
        
        # Insert data into NotificationLog table
        cursor.execute("INSERT INTO NotificationLog (UserID, NotificationType, NotificationContent, NotificationDateTime) VALUES (%s, %s, %s, %s)", (user_id, notification_type, notification_content, notification_date_time))
        db.commit()
        return redirect('/view_notification_logs')
    else:
        return render_template('add_notification_log.html')

@app.route('/update_notification_log/<int:log_id>', methods=['GET', 'POST'])
def update_notification_log(log_id):
    if request.method == 'POST':
        # Retrieve form data
        user_id = request.form['user_id']
        notification_type = request.form['notification_type']
        notification_content = request.form['notification_content']
        notification_date_time = request.form['notification_date_time']
        
        # Update data in NotificationLog table
        cursor.execute("UPDATE NotificationLog SET UserID=%s, NotificationType=%s, NotificationContent=%s, NotificationDateTime=%s WHERE LogID=%s", (user_id, notification_type, notification_content, notification_date_time, log_id))
        db.commit()
        return redirect('/view_notification_logs')
    else:
        cursor.execute("SELECT * FROM NotificationLog WHERE LogID=%s", (log_id,))
        log = cursor.fetchone()
        return render_template('update_notification_log.html', log=log)

@app.route('/delete_notification_log/<int:log_id>')
def delete_notification_log(log_id):
    cursor.execute("DELETE FROM NotificationLog WHERE LogID=%s", (log_id,))
    db.commit()
    return redirect('/view_notification_logs')

#ScheduledTasks CRUD Routes
@app.route('/view_scheduled_tasks')
def view_scheduled_tasks():
    cursor.execute("SELECT * FROM ScheduledTasks")
    scheduled_tasks = cursor.fetchall()
    return render_template('view_scheduled_tasks.html', scheduled_tasks=scheduled_tasks)

@app.route('/add_scheduled_task', methods=['GET', 'POST'])
def add_scheduled_task():
    if request.method == 'POST':
        # Retrieve form data
        task_name = request.form['task_name']
        task_description = request.form['task_description']
        scheduled_time = request.form['scheduled_time']
        device_id = request.form['device_id']
        
        # Insert data into ScheduledTasks table
        cursor.execute("INSERT INTO ScheduledTasks (TaskName, TaskDescription, ScheduledTime, DeviceID) VALUES (%s, %s, %s, %s)", (task_name, task_description, scheduled_time, device_id))
        db.commit()
        return redirect('/view_scheduled_tasks')
    else:
        return render_template('add_scheduled_task.html')

@app.route('/update_scheduled_task/<int:task_id>', methods=['GET', 'POST'])
def update_scheduled_task(task_id):
    if request.method == 'POST':
        # Retrieve form data
        task_name = request.form['task_name']
        task_description = request.form['task_description']
        scheduled_time = request.form['scheduled_time']
        device_id = request.form['device_id']
        
        # Update data in ScheduledTasks table
        cursor.execute("UPDATE ScheduledTasks SET TaskName=%s, TaskDescription=%s, ScheduledTime=%s, DeviceID=%s WHERE TaskID=%s", (task_name, task_description, scheduled_time, device_id, task_id))
        db.commit()
        return redirect('/view_scheduled_tasks')
    else:
        cursor.execute("SELECT * FROM ScheduledTasks WHERE TaskID=%s", (task_id,))
        task = cursor.fetchone()
        return render_template('update_scheduled_task.html', task=task)

@app.route('/delete_scheduled_task/<int:task_id>')
def delete_scheduled_task(task_id):
    cursor.execute("DELETE FROM ScheduledTasks WHERE TaskID=%s", (task_id,))
    db.commit()
    return redirect('/view_scheduled_tasks')

#Delete Routes
if __name__ == '__main__':
    app.run(debug=True)