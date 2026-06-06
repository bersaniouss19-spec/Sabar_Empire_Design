from .models import Robot

def run_analysis_for_robot(robot_id):
    # Récupère le robot dans la base de données
    robot = Robot.objects.get(id=robot_id)

    # Exécute l'analyse avec le moteur viral que tu viens de coller
    # (full_virality_report est maintenant disponible dans ce fichier)
    report = full_virality_report(robot.contenu_a_analyser)

    # Sauvegarde les résultats dans ton modèle Django
    robot.score_viral_global = report['global_virality_score']
    robot.save()

    return report